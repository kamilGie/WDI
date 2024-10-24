from typing import List, Callable


class Bazowa:
    """
    Klasa Bazowa do generowania kodu na podstawie prototypu zadania.

    Attributes:
        nr_zadania (int): Numer zadania.
        funkcje (List[Callable]): Lista funkcji do użycia w kodzie.
        linie_prototypu (List[str]): Linijki kodu prototypu.
        sciezka (str): Ścieżka do folderu z generowanym kodem.
        res (str): Zbierany wygenerowany kod.
    """

    def __init__( self, linie_prototypu: List[str], nr_zadania: int, funkcje: List[Callable], sciezka_zadania: str):
        """Inicjalizuje obiekt klasy Bazowa."""
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka = sciezka_zadania
        self.res = ""

    def generuj(self):
        """Generuje kod na podstawie prototypu bez funkcji stworz zadanie."""
        for linia in self.linie_prototypu:
            if "stworz_zadanie" not in linia and "komenda(" not in linia:
                self.res += linia
