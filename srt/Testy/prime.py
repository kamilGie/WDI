import inspect
import io
from contextlib import redirect_stdout
from Bazowa import Bazowa
from typing import Callable, Tuple, Any
from copy import deepcopy

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
                if parametry == tuple("stop"):
                    break
                wynik_funkcji, czy_wynik_w_print = self.wynik_wykonania_funkcji(
                    funkcja, parametry
                )
            except Exception as e:
                print(f"{str(e)} Wprowadz Ponownie!")
                continue

            metoda_testowa = self._wybierz_metode_testowa(czy_wynik_w_print, funkcja)
            self.res += metoda_testowa(
                funkcja.__name__,
                nr_testu,
                parametry,
                wynik_funkcji,
                self.nazwi_zmienne(parametry),
            )
            self.res += "\n"

            if liczba_argumentow == 0:
                print(f"Wynik to {wynik_funkcji}")
                break

            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")
            nr_testu += 1

        print("\n")

    def _wybierz_metode_testowa(self, czy_wynik_w_print, funkcja):
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

    def pobierz_parametry(self, test_index: int, param_count: int) -> Tuple:
        """
        Pobiera parametry testowe od użytkownika.

        Args:
            test_index (int): Indeks aktualnego testu.
            param_count (int): Liczba argumentów, które mają być pobrane.

        Returns:
            Tuple: Krotka z parametrami podanymi przez użytkownika.
        """
        if param_count == 0:
            return ()
        else:
            koncowka_argumetnow = "" if 1 == param_count else "y"
            wyjscie = ", lub 'stop' by zakonczyc testy" if test_index > 3 else ""
            wejscie = input(
                f"\nTest nr {test_index}\nPodaj {param_count} argument{koncowka_argumetnow} testowe{wyjscie}: "
            )
            if wejscie == "stop":
                return tuple("stop")
        print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")
        return tuple(self.przetwarzaj_wejscie(wejscie))

    def konwertuj_argument(self, arg):
        """Konwertuje argument na odpowiedni typ: int, float,str lub pozostaje czysty"""
        for typ in (int, float):
            try:
                return typ(arg)
            except ValueError:
                continue
        return arg

    def przetwarzaj_stringa(self, argumenty, i, dodaj_cudzyslow=True):
        """
        Przetwarza napis z argumentów w formie tekstowej, obsługując spacje.

        Args:
            argumenty (list): Lista argumentów w formie tekstowej.
            i (int): Indeks aktualnego argumentu do przetworzenia.

        Returns:
            tuple: Krotka zawierająca:
                - wynik (str): Przetworzony napis.
                - i (int): Zaktualizowany indeks po przetworzeniu napisu.
        """
        typ_cudzyslowu = argumenty[i]
        i += 1
        fragmenty = []

        try:
            while argumenty[i] != typ_cudzyslowu:
                fragmenty.append(argumenty[i])
                i += 1
        except IndexError:
            raise ValueError(
                f"Nie zamknięty znak stringa dla cudzysłowu: {typ_cudzyslowu}"
            )

        wynik = " ".join(fragmenty)
        if dodaj_cudzyslow:
            wynik = typ_cudzyslowu + wynik + typ_cudzyslowu
        return wynik, i

    def przetwarzaj_tablice(self, argumenty, i):
        """
        Przetwarza tablicę z argumentów w formie tekstowej, obsługując zagnieżdżone tablice.

        Args:
            argumenty (list): Lista argumentów w formie tekstowej, w której mogą występować zagnieżdżone tablice.
            i (int): Indeks aktualnego argumentu do przetworzenia.

        Returns:
            tuple: Krotka zawierająca:
                - wynik (list): Przetworzona tablica, która może zawierać inne tablice jako elementy.
                - i (int): Zaktualizowany indeks po przetworzeniu tablicy.
        """
        wynik = []
        i += 1

        while argumenty[i] != "]":
            if argumenty[i] == "[":  # znaleziono nową tablicę
                tablica, i = self.przetwarzaj_tablice(argumenty, i)
                wynik.append(tablica)
            elif argumenty[i] == '"' or argumenty[i] == "'":
                napis, i = self.przetwarzaj_stringa(argumenty, i, dodaj_cudzyslow=False)
                wynik.append(napis)
            else:
                wynik.append(self.konwertuj_argument(argumenty[i]))
            i += 1

        return wynik, i

    def przetwarzaj_wejscie(self, wejscie):
        """
        Przetwarza wejście w formie tekstowej na strukturę danych (listę), obsługując zagnieżdżone tablice.

        Args:
            wejscie (str): Tekstowe wejście do przetworzenia, zawierające argumenty i tablice.

        Returns:
            list: Lista przetworzonych argumentów, gdzie tablice są reprezentowane jako zagnieżdżone listy.
        """
        # W przyszlosci mozliwe ze projekt przejdzie  na wyrazenia regularne ale narazie dla czytelnosci zostawiam to
        wejscie = (
            wejscie.replace(",", " ")
            .replace("]", " ] ")
            .replace("[", " [ ")
            .replace("'", " ' ")
            .replace('"', ' " ')
            .replace("(", " [ ")
            .replace(")", " ] ")
            .replace("\n", " ")
        )
        argumenty = wejscie.split()

        przetwarzaj = {
            "[": self.przetwarzaj_tablice,
            '"': self.przetwarzaj_stringa,
            "'": self.przetwarzaj_stringa,
        }

        wyniki = []
        i = 0
        while i < len(argumenty):
            if argumenty[i] in przetwarzaj:
                element, i = przetwarzaj[argumenty[i]](argumenty, i)
                wyniki.append(element)
            else:
                wyniki.append(self.konwertuj_argument(argumenty[i]))
            i += 1

        return wyniki

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
        parametry_kopia = [
            p[1:-1] if isinstance(p, str) and p[1] == "'" or p[0] == '"' else p
            for p in parametry
        ]

        f = io.StringIO()
        with redirect_stdout(f):
            wynik = funkcja(*parametry_kopia)
        if wynik is None:
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
