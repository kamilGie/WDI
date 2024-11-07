from prime import prime

from typing import Callable
import inspect
from random import randint


class Agent:
    def __init__(self, liczba_argumentow) -> None:
        self.liczba_argumentow = liczba_argumentow

    def generuj_testy(self):
        for _ in range(30):
            losowe_argumenty = tuple(
                randint(-100, 1000) for _ in range(self.liczba_argumentow)
            )
            yield losowe_argumenty


class ai(prime):

    def generuj_testy_dla_funkcji(self, funkcja: Callable):
        liczba_argumentow = len(inspect.signature(funkcja).parameters)
        if liczba_argumentow == 0:
            super().generuj_testy_dla_funkcji(funkcja)

        agent = Agent(liczba_argumentow)

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
