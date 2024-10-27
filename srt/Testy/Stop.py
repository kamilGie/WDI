import inspect
from Prime import Prime, Tuple

from typing import Callable

from _utils_T import metoda_nasluchujaca_testow, metoda_zwracajaca_testow


class Stop(Prime):
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

            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")
            if isinstance(wynik_funkcji, str):
                self.res += metoda_nasluchujaca_testow(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )
            else:
                self.res += metoda_zwracajaca_testow(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )
            nr_testu += 1

        print("\n")

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
            return ()  # Zwróć pustą krotkę, gdy nie ma argumentów
        elif param_count == 1:
            wejscie = input(f"\ntest nr {test_index} Podaj argument testowy: ")
        else:
            wejscie = input(
                f"\ntest nr {test_index} Podaj {param_count} argumenty testowe, oddzielone spacją: "
            )
        if wejscie == "stop":
            return tuple("stop")
        print(f"\033[F\033[K\033[F\033[K", end="")
        return tuple(self.przetwarzaj_wejscie(wejscie))
