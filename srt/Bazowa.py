from abc import abstractmethod
import os
from typing import List, Callable


class Bazowa:
    """
    Klasa ta jest odpowiedzialna za generowanie Szablonu w oparciu o linie prototypu
    oraz funkcje, które są dostarczane podczas jej inicjalizacji.

    Attributes:
        nr_zadania (int): Numer zadania, dla którego generowany jest kod.
        funkcje (List[Callable]): Lista funkcji, które mają być używane w kodzie.
        linie_prototypu (List[str]): Linijki kodu prototypu zadania.
        sciezka (str): Ścieżka do folderu, w którym będzie zapisany generowany kod.
    """

    def __init__( self, linie_prototypu: list[str], nr_zadania: str, funkcje: List[Callable], sciezka_zadania: str,):
        """
        Args:
            linie_prototypu (List[str]): Lista linijek kodu prototypu.
            nr_zadania (int): Numer zadania, dla którego generowany jest kod.
            funkcje (List[Callable]): Lista funkcji do użycia w generowanym kodzie.
            sciezka_zadania (str): Ścieżka do folderu, w którym będzie zapisany generowany kod.
        """
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka_zadnia = sciezka_zadania
        self.nazwa_pliku: str = f"{os.path.dirname(os.path.abspath(__file__)).lower()}{nr_zadania}.py"

    @abstractmethod
    def generuj(self) -> str:
        pass
