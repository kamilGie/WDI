import inspect
import io
from contextlib import redirect_stdout
from Bazowa import Bazowa
from typing import Callable, Tuple, Any

from _utils_T import (
    IMPORTY,
    KOMENDA,
    NAGLOWEK,
    ODPAL_TESTY,
    dynamiczny_import_funkcji,
    RAMKA,
)


class prime(Bazowa):
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

        liczba_argumentow = len(inspect.signature(funkcja).parameters)

        nr_testu = 1
        while True:
            try:
                parametry = self.pobierz_parametry(nr_testu, liczba_argumentow)
                if parametry == "stop":
                    break
                wynik_funkcji, czy_wynik_w_print = self.wynik_wykonania_funkcji(
                    funkcja, parametry
                )
            except Exception as e:
                print(f"{str(e)} Wprowadz Ponownie!")
                continue

            metoda_testowa = self._wybierz_metode_testowa(czy_wynik_w_print, funkcja)
            self.res += metoda_testowa(
                funkcja.__name__, nr_testu, parametry, wynik_funkcji
            )
            self.res += "\n"

            if liczba_argumentow == 0:
                print(f"Wynik to {wynik_funkcji}")
                break

            print(f"Dla {parametry} wynik to {wynik_funkcji}")
            nr_testu += 1

        print("\n")

    def _wybierz_metode_testowa(self, czy_wynik_w_print, funkcja):
        """Wybiera odpowiednią metodę testową na podstawie flagi."""
        return (
            self.metoda_nasluchujaca_testow
            if czy_wynik_w_print
            else self.metoda_zwracajaca_testow
        )

    def metoda_zwracajaca_testow(self, NazwaTestu, numerTestu, zmienne, wynikWywolania):
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
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}(self):
            self.assertEqual({NazwaTestu}({zmienne}), {wynikWywolania})\n"""

    def metoda_nasluchujaca_testow(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania
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
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({zmienne})
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, {wynikWywolania})\n"""

    def pobierz_parametry(self, test_index: int, param_count: int) -> str:
        """
        Pobiera parametry testowe od użytkownika.

        Args:
            test_index (int): Indeks aktualnego testu.
            param_count (int): Liczba argumentów, które mają być pobrane.

        Returns:
            Tuple: Krotka z parametrami podanymi przez użytkownika.
        """
        if param_count == 0:
            return ""

        koncowka_argumetnow = "" if 1 == param_count else "y"
        wyjscie = ", lub 'stop' by zakonczyc testy" if test_index > 3 else ""
        wejscie = input(
            f"\nTest nr {test_index}\nPodaj {param_count} argument{koncowka_argumetnow} testowe{wyjscie}: "
        )
        print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")
        return wejscie

    def wynik_wykonania_funkcji(
        self, funkcja: Callable, parametry: str
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
            wynik = funkcja(*eval(f"[{parametry}]"))
        if wynik is None:
            return repr(f.getvalue().strip()), True
        elif isinstance(wynik, str):
            wynik = f'"{wynik}"'

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
