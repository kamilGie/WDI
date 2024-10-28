from Prime import Prime

from typing import Callable
import inspect
from _utils_T import (
    metoda_zwracajaca_testow_bez_kolejnosci,
    metoda_nasluchujaca_testow_bez_kolejnosci,
)


class bez_kolejnosci(Prime):
    def generuj_testy_dla_funkcji(self, funkcja: Callable):
        """
        Generuje testy dla konkretnej funkcji.

        Args:
            funkcja (Callable): Funkcja, dla której mają być generowane testy.
        """
        if len(self.funkcje) > 1:
            print(f"\ttesty dla funkcji {funkcja.__name__}\n")

        liczba_argumentow = len(inspect.signature(funkcja).parameters)

        nr_testu = 1
        while nr_testu <= liczba_argumentow * 20 + 1:
            try:
                parametry = self.pobierz_parametry(nr_testu, liczba_argumentow)
                wynik_funkcji = self.wynik_funkcje(funkcja, parametry)
            except Exception as e:
                print(f"{str(e)} Wprowadz Ponownie!")
                continue

            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")
            if isinstance(wynik_funkcji, str):
                self.res += metoda_nasluchujaca_testow_bez_kolejnosci(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )
            else:
                self.res += metoda_zwracajaca_testow_bez_kolejnosci(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )
            nr_testu += 1

        print("\n")
