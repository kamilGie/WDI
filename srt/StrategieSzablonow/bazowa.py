from typing import List, Callable

from _utils_S import main, parsuj_prototyp


class bazowa:
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
        linie_prototypu: list[str],
        nr_zadania: int,
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

    def generuj(self) -> str:
        """
        Generuje kod na podstawie prototypu oraz dostarczonych funkcji.

        Kod jest generowany poprzez iterację przez linie prototypu,
        zbierając odpowiednie linie oraz informacje o funkcjach.

        - Linijki zaczynające plik z "#" są dodawane do rezultatu jako komentarze.
        - Linijki z definicjami funkcji ktore byly przekazane do funkcji jako istotne
          są dodawane do rezultatu z dodatkowymi informacjami.
        - Na końcu generowany jest blok `if __name__ == "__main__":`,
        - oraz import odpal_testy wraz  z wywolaniem zakomentowanym
        """
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje)
        res += main(self.nr_zadania)
        return res
