""" 
    to dopiero jest pisane i raczej daleka droga przed tym generatorem
"""

from collections import deque
from torch.optim.adam import Adam
from itertools import product
from prime import prime
import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Callable
import inspect
from random import sample
import time
from coverage import Coverage

learning_rate = 5e-4
minbatch_size = 100
gamma = 0.99
repley_bufer_size = int(1e5)
interpolation_parameter = 1e-3


class Network(nn.Module):
    def __init__(self, action_size) -> None:
        super(Network, self).__init__()

        self.fc1 = nn.Linear(3, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size * 1100)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        return self.fc3(x)


class ReplayMemory(object):

    def __init__(self, capacity) -> None:
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.capacity = capacity
        self.memory = []

    def push(self, event):
        self.memory.append(event)
        if len(self.memory) > self.capacity:
            del self.memory[0]

    def sample(self, batch_size):
        experiences = sample(self.memory, k=batch_size)
        states = (
            torch.from_numpy(np.vstack([e[0] for e in experiences if e is not None]))
            .float()
            .to(self.device)
        )
        actions = (
            torch.from_numpy(np.vstack([e[1] for e in experiences if e is not None]))
            .long()
            .to(self.device)
        )
        rewards = (
            torch.from_numpy(np.vstack([e[2] for e in experiences if e is not None]))
            .float()
            .to(self.device)
        )
        return states, actions, rewards


class Agent:
    def __init__(self, liczba_argumentow) -> None:
        self.liczba_argumentow = liczba_argumentow
        self.action_size = liczba_argumentow * 1100
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.liczba_argumentow = liczba_argumentow
        self.local_qnetwork = Network(self.action_size)
        self.target_qnetwork = Network(self.action_size)
        self.optimizer = Adam(self.local_qnetwork.parameters(), lr=learning_rate)
        self.memory = ReplayMemory(repley_bufer_size)
        self.t_step = 0

    def step(self, state, action, reward):
        self.memory.push((state, action, reward))
        self.t_step += 1
        self.t_step %= 4
        if self.t_step == 0:
            if len(self.memory.memory) > minbatch_size:
                experienes = self.memory.sample(100)
                self.learn(experienes)

    def act(self, state, epsilon=0.0):
        state = np.array(state)
        state = torch.from_numpy(state).float().unsqueeze(0).to(self.device)
        self.local_qnetwork.eval()
        with torch.no_grad():
            action_values = self.local_qnetwork(state)
        self.local_qnetwork.train()
        if random.random() > epsilon:
            return np.argmax(action_values.cpu().data.numpy())
        else:
            return random.choice(np.arange(self.action_size))

    def learn(self, experiences):
        states, actions, rewards = experiences

        q_targets = rewards  # Wartości docelowe będą równe nagrodom

        q_expected = self.local_qnetwork(states).gather(1, actions)

        loss = F.mse_loss(q_expected, q_targets)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        self.soft_update(
            self.local_qnetwork, self.target_qnetwork, interpolation_parameter
        )

    def soft_update(self, local_model, target_model, interpolation_parameter):
        for target_param, local_param in zip(
            target_model.parameters(), local_model.parameters()
        ):
            target_param.data.copy_(
                interpolation_parameter * local_param.data
                + (1.0 - interpolation_parameter) * target_param.data
            )

    def generuj_testy(self):
        values = np.arange(1.0, -1.1, -0.5)
        all_combinations = list(product(values, repeat=3))
        for state in all_combinations:
            action = self.act(state, 0.01) - 100
            yield tuple(
                action,
            )


class ai(prime):

    def generuj_testy_dla_funkcji(self, funkcja: Callable):
        liczba_argumentow = len(inspect.signature(funkcja).parameters)
        if liczba_argumentow == 0:
            super().generuj_testy_dla_funkcji(funkcja)

        epsilon_starting_value = 1
        epsilon_ending_value = 0.01
        epsilon_decay_value = 0.995
        epsilon = epsilon_starting_value
        scores_on_100_episodes = deque(maxlen=100)
        agent = Agent(liczba_argumentow)

        values = np.arange(1.0, -1.1, -0.2)
        all_combinations = list(product(values, repeat=3))
        for state in all_combinations:
            for _ in range(100):
                score = 0

                action = agent.act(state, epsilon) - 100

                if not isinstance(state, np.ndarray):
                    state = np.array(state, dtype=np.float64)

                # Upewnijmy się, że state ma co najmniej 3 elementy
                if len(state) < 3:
                    raise ValueError("State must have at least 3 elements")

                # Teraz wykonujemy operację mnożenia, gdy state jest tablicą NumPy
                cov = Coverage()
                cov.start()
                start_time = time.time()
                wynik = funkcja(action)
                czas_wykonywania = time.time() - start_time
                cov.stop()
                cov.save()

                filename = inspect.getfile(funkcja)  # Pobieramy ścieżkę pliku
                przechodniosci = cov.analysis(filename)[1]

                # Teraz wykonujemy mnożenie
                reward = (
                    przechodniosci * state[0]
                    + wynik * state[1]
                    + czas_wykonywania * state[2]
                )

                # Zaktualizowanie agenta
                agent.step(state, action, reward)

                score += reward
                scores_on_100_episodes.append(score)
                epsilon = max(epsilon_ending_value, epsilon_decay_value * epsilon)

            print(
                "\rEpisode {}\tAverage Score: {:.2f}".format(
                    len(scores_on_100_episodes), np.mean(scores_on_100_episodes)
                ),
                end="",
            )

        nr_testu = 1
        for parametry in agent.generuj_testy():
            wynik_funkcji, czy_wynik_w_print = self.wynik_wykonania_funkcji(
                funkcja, parametry
            )
            metoda_testowa = self._wybierz_metode_testowa(czy_wynik_w_print, funkcja)
            self.res += metoda_testowa(
                funkcja.__name__,
                nr_testu,
                parametry,
                wynik_funkcji,
                self.nazwi_zmienne(parametry),
            )
            self.res += "\n"

            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")
            nr_testu += 1

        while True:
            czy_dodac_testy = input("czy chcesz dodac wlasne testy ? (y/n)")
            if czy_dodac_testy == "y" or czy_dodac_testy == "n":
                break

        if czy_dodac_testy == "y":
            super().generuj_testy_dla_funkcji(funkcja)
