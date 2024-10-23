import inspect
import io
from contextlib import redirect_stdout
from _utils_T import DolKlasyTestow, MetodaKlasyTestow, GoraKlasyTestow, RAMKA
from typing import List, Callable, Tuple, Any


class Bazowa:
    def __init__(
        self,
        linie_prototypu: List[str],
        nr_zadania: int,
        funkcje: List[Callable],
        sciezka_zadania: str,
    ):
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka = sciezka_zadania
        self.res = ""

    def generuj(self):
        print(f"\nPisanie testów dla zadania nr: {self.nr_zadania}\n{RAMKA}")
        self.res += GoraKlasyTestow(self.nr_zadania, self.funkcje)
        for funkcja in self.funkcje:
            self.generuj_testy_dla_funkcji(funkcja)
        self.finalizuj_testy()

    def generuj_testy_dla_funkcji(self, funkcja: Callable):
        if len(self.funkcje) > 1:
            print(f"\ttesty dla funkcji {funkcja.__name__}\n")

        liczba_argumentow = len(inspect.signature(funkcja).parameters)

        i = 1
        while i <= liczba_argumentow * 10 + 1:
            try:
                parametry = self.pobierz_parametry(i, liczba_argumentow)
                wynik_funkcji = self.uruchom_funkcje(funkcja, parametry)
            except Exception as e:
                print(f"{str(e)} Wprowadz Ponownie!")
                continue

            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")
            self.res += MetodaKlasyTestow(funkcja.__name__, i, parametry, wynik_funkcji)
            i += 1

        print("\n")

    def pobierz_parametry(self, test_index: int, param_count: int) -> Tuple:
        if param_count == 0:
            return ()  # Zwróć pustą krotkę, gdy nie ma argumentów
        elif param_count == 1:
            wejscie = input(f"\ntest nr {test_index} Podaj argument testowy: ")
        else:
            wejscie = input(
                f"\ntest nr {test_index} Podaj {param_count} argumenty testowe, oddzielone spacją: "
            )
        print(f"\033[F\033[K\033[F\033[K", end="")
        return tuple(map(int, wejscie.split()))

    def uruchom_funkcje(self, funkcja: Callable, parametry: Tuple) -> Any:
        f = io.StringIO()
        with redirect_stdout(f):
            funkcja(*parametry)
        return repr(f.getvalue().strip())

    def finalizuj_testy(self):
        print(RAMKA, end="")
        print(f"🥳 Testy dla zadania {self.nr_zadania} zostały pomyślnie wygenerowane!")
        print(
            f"\tNalezy sprawdzic czy folder zadania wyglada poprawnie i usunac prototyp"
        )
        print(RAMKA)
        self.res += "\n"
        self.res += DolKlasyTestow(self.nr_zadania)
