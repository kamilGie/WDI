from typing import List, Callable


class bazowa:
    """
    Klasa Bazowa do generowania kodu na podstawie prototypu zadania.

    Attributes:
        nr_zadania (int): Numer zadania.
        funkcje (List[Callable]): Lista funkcji do użycia w kodzie.
        linie_prototypu (List[str]): Linijki kodu prototypu.
        sciezka (str): Ścieżka do folderu z generowanym kodem.
        res (str): Zbierany wygenerowany kod.
    """

    def __init__(
        self,
        linie_prototypu: List[str],
        nr_zadania: int,
        funkcje: List[Callable],
        sciezka_zadania: str,
    ):
        """Inicjalizuje obiekt klasy Bazowa."""
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka_zadania = sciezka_zadania

    def generuj(self) -> str:
        """Generuje kod na podstawie prototypu bez maina."""
        res = ""
        for linia in self.linie_prototypu:
            if 'if __name__ == "__main__":' in linia:
                return res
            res += linia
        return res
