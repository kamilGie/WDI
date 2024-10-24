from _utils_S import FunkcjaInput
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
        res (str): Zbiera wygenerowany kod jako string.
    """

    def __init__(
        self,
        linie_prototypu: list[str],
        nr_zadania: int,
        funkcje: List[Callable],
        sciezka_zadania: str,
    ):
        """
        Inicjalizuje obiekt klasy Bazowa.

        Args:
            linie_prototypu (List[str]): Lista linijek kodu prototypu.
            nr_zadania (int): Numer zadania, dla którego generowany jest kod.
            funkcje (List[Callable]): Lista funkcji do użycia w generowanym kodzie.
            sciezka_zadania (str): Ścieżka do folderu, w którym będzie zapisany generowany kod.
        """
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka = sciezka_zadania
        self.res = ""

    def generuj(self):
        """
        Generuje kod na podstawie prototypu oraz dostarczonych funkcji.

        Kod jest generowany poprzez iterację przez linie prototypu,
        zbierając odpowiednie linie oraz informacje o funkcjach.

        - Linijki zaczynające się od "#" są dodawane do rezultatu jako komentarze.
        - Linijki z definicjami funkcji są dodawane do rezultatu z dodatkowymi informacjami.
        - Na końcu generowany jest blok `if __name__ == "__main__":`,
          gdzie importowane są testy dla danego zadania oraz wywoływane funkcje.
        """
        wstep = True
        for linia in self.linie_prototypu:
            if wstep:
                if linia.strip().startswith("#"):
                    self.res += linia
                else:
                    wstep = False
            elif any(linia.startswith(f"def {f.__name__}") for f in self.funkcje):
                self.res += "\n\n" + linia.replace("\n", "") + " ...\n\n"
            elif 'if __name__ == "__main__":\n' in linia:
                break

        self.res += '\nif __name__ == "__main__":\n'
        self.res += f"    from testy{self.nr_zadania} import Testy{self.nr_zadania}\n\n"
        for funkcja in self.funkcje:
            self.res += FunkcjaInput(funkcja)
        self.res += f"\n    # Testy{self.nr_zadania}.Uruchom()\n"
