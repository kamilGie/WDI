from prime import prime

from typing import Callable
import inspect
from _utils_T import (
    metoda_zwracajaca_testow_bez_kolejnosci,
    metoda_nasluchujaca_testow_bez_kolejnosci,
)


class bez_kolejnosci(prime):
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
        while True:
            try:
                parametry = self.pobierz_parametry(nr_testu, liczba_argumentow)
                if parametry == tuple("stop"):
                    break
                wynik_funkcji = self.wynik_funkcje(funkcja, parametry)
            except Exception as e:
                print(f"{str(e)} Wprowadz Ponownie!")
                continue

            if isinstance(wynik_funkcji, str):
                self.res += metoda_nasluchujaca_testow_bez_kolejnosci(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )
            else:
                self.res += metoda_zwracajaca_testow_bez_kolejnosci(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )

            if liczba_argumentow == 0:
                print(f"Wynik to {wynik_funkcji}")
                break

            nr_testu += 1
            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")

        print("\n")
