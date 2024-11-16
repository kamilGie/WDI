from abc import abstractmethod
import os
from typing import List, Callable
import inspect


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

    def __init__(
        self,
        linie_prototypu: List[str],
        nr_zadania: str,
        funkcje: List[Callable],
        sciezka_zadania: str,
    ):
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
        # bierze Folder klasy do ktorej nalezy i z tego bierze nazwe pliku
        nazwa_folderu = os.path.basename(
            os.path.dirname(os.path.abspath(inspect.getfile(self.__class__)))
        )
        self.nazwa_pliku: str = f"{nazwa_folderu.lower()}{nr_zadania}.py"

    @abstractmethod
    def __str__(self) -> str:
        """Abstrakcyjna metoda do generowania tekstowej reprezentacji obiektu."""
        pass
