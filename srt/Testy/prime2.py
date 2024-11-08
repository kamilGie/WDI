import inspect
import os
import sys
import io
from contextlib import redirect_stdout
from Bazowa import Bazowa
from typing import Callable, Tuple, Any, List

from _utils_t import (
    RAMKA,
    ODPAL_TESTY,
    NAGLOWEK,
    IMPORTY,
    KOMENDA,
    dynamiczny_import_funkcji,
)


class prime2(Bazowa):
    def __init__(
        self,
        linie_prototypu: list[str],
        nr_zadania: str,
        funkcje: List[Callable],
        sciezka_zadania: str,
    ):
        super().__init__(linie_prototypu, nr_zadania, funkcje, sciezka_zadania)
        sys.path.append(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "generatory_argumentow"
            )
        )
        from generatory_argumentow.input import pobierz_parametry
        from generatory_argumentow.przedzial_losowo_typowy import wygeneruj_losowe_testy

        self.genratory = [wygeneruj_losowe_testy, pobierz_parametry]

    def __str__(self) -> str:
        """
        Generuje testy dla zadania, wywołując odpowiednie metody w celu utworzenia
        struktury testów i ich wyników.
        """
        print(f"\nPisanie testów dla zadania nr: {self.nr_zadania}\n{RAMKA}")

        self.res = IMPORTY
        self.res += "\n"
        self.res += dynamiczny_import_funkcji(self.nr_zadania, self.funkcje)
        self.res += "\n\n"
        self.res += ODPAL_TESTY
        self.res += "\n"
        self.res += KOMENDA
        self.res += "\n\n"
        self.res += NAGLOWEK
        self.res += "\n"

        for funkcja in self.funkcje:
            self.generuj_testy_dla_funkcji(funkcja)

        self.finalizuj_testy()
        return self.res

    def generuj_testy_dla_funkcji(self, funkcja: Callable):
        """
        Generuje testy dla konkretnej funkcji.

        Args:
            funkcja (Callable): Funkcja, dla której mają być generowane testy.
        """
        if len(self.funkcje) > 1:
            print(f"\ttesty dla funkcji {funkcja.__name__}\n")

        # Jesli nie ma parametrow to nie bedziemy generowac argumentow
        if len(inspect.signature(funkcja).parameters) == 0:
            wynik_funkcji, czy_wynik_w_print = self.wynik_wykonania_funkcji(funkcja, ())
            metoda_testowa = self._wybierz_metode_testowa(czy_wynik_w_print, funkcja)
            self.res += metoda_testowa(funkcja.__name__, 1, (), wynik_funkcji, [""])
            print(f"Wynik to {wynik_funkcji}\n")
            return

        nr_testu = 1
        for generator in self.genratory:

            for parametr in generator(funkcja, nr_testu):
                try:
                    wynik_funkcji, czy_wynik_w_print = self.wynik_wykonania_funkcji(
                        funkcja, parametr
                    )
                except Exception as e:
                    print(f"{str(e)}!")
                    continue

                metoda_testowa = self._wybierz_metode_testowa(
                    czy_wynik_w_print, funkcja
                )
                self.res += metoda_testowa(
                    funkcja.__name__,
                    nr_testu,
                    parametr,
                    wynik_funkcji,
                    self.nazwi_zmienne(parametr),
                )
                self.res += "\n"

                print(f"Dla {', '.join(map(str, parametr))} wynik to {wynik_funkcji}")
                nr_testu += 1

            print("\n")

    def dodaj_typowe_wartosci(self, dol, gora):
        """generator typowe wartosci testow dla przedzialu"""
        typowe_wartosci = [0, 1, -1, 10]

        for wartosc in typowe_wartosci:
            if all(d <= wartosc for d in dol) and all(g > wartosc for g in gora):
                yield tuple([wartosc] * len(dol))

    def _wybierz_metode_testowa(self, czy_wynik_w_print, _):
        """Wybiera odpowiednią metodę testową na podstawie flagi."""
        return (
            self.metoda_nasluchujaca_testow
            if czy_wynik_w_print
            else self.metoda_zwracajaca_testow
        )

    def metoda_zwracajaca_testow(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        """
        Generuje kod testu jednostkowego dla metody zwracającej wynik.

        Args:
            NazwaTestu (str): Nazwa testowanej funkcji.
            numerTestu (int): Numer testu, który będzie użyty w nazwie testu.
            zmienne : Lista argumentów przekazywanych do funkcji.
            wynikWywolania: Oczekiwany wynik wywołania funkcji.
            zmienne_nazwa str: napis nazw zmiennych użytych jako argumenty.

        Returns:
            str: Kod testu jednostkowego w formacie tekstowym.
        """
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            self.assertEqual({NazwaTestu}({', '.join(map(str, zmienne))}), {wynikWywolania})\n"""

    def metoda_nasluchujaca_testow(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        """
        Generuje kod testu jednostkowego dla metody, która nasłuchuje wyników na standardowym wyjściu.

        Args:
            NazwaTestu (str): Nazwa testowanej funkcji.
            numerTestu (int): Numer testu, który będzie użyty w nazwie testu.
            zmienne : Lista argumentów przekazywanych do funkcji.
            wynikWywolania: Oczekiwany wynik wywołania funkcji na standardowym wyjściu.
            zmienne_nazwa str: napis nazw zmiennych użytych jako argumenty.

        Returns:
            str: Kod testu jednostkowego w formacie tekstowym, który sprawdza standardowe wyjście funkcji.
        """
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, {wynikWywolania})\n"""

    def nazwi_zmienne(self, zmienne):
        def przetworz_zmienna(z):
            nazwa = ""
            if isinstance(z, (int, float)):
                nazwa = f"minus_{abs(z)}" if z < 0 else str(z)
                if isinstance(z, float):
                    nazwa = nazwa.replace(".", "_")
                    nazwa += "f"

            elif isinstance(z, list):
                # Sprawdzamy, czy to zagnieżdżona lista
                nazwa = "tablica"
            return nazwa

        zmienne_nazwa = [przetworz_zmienna(z) for z in zmienne]
        return zmienne_nazwa

    def wynik_wykonania_funkcji(
        self, funkcja: Callable, parametry: Tuple
    ) -> Tuple[Any, bool]:
        """
        Uruchamia podaną funkcję z przekazanymi parametrami i przechwycuje jej wynik.

        Args:
            funkcja (Callable): Funkcja do uruchomienia.
            parametry (Tuple): Argumenty przekazywane do funkcji.

        Returns:
            Any: Zwraca wynik funkcji
            bool: Flaga wskazująca, czy wynik został zwrócony przez funkcję (False),
                  czy był wyprintowany na standardowe wyjście (True).
        """
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = funkcja(*parametry)
        if wynik == None:
            return repr(f.getvalue().strip()), True

        return wynik, False

    def finalizuj_testy(self):
        """
        Finalizuje proces generacji testów, wyświetla podsumowanie oraz zapisuje
        wyniki do atrybutu `res`.
        """
        print(RAMKA, end="")
        print(f"🥳 Testy dla zadania {self.nr_zadania} zostały pomyślnie wygenerowane!")
        print(RAMKA)
        self.res += "\n"
