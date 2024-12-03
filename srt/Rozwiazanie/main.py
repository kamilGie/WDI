from Bazowa import Bazowa

from typing import List, Callable
import os


class main(Bazowa):
    """Wszystko z prototypu po za linijami zawierajacymi `stworz_zadanie` oraz `komenda(`"""

    def __init__(
        self,
        linie_prototypu: List[str],
        nr_zadania: str,
        funkcje: List[Callable],
        sciezka_zadania: str,
    ):
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka_zadnia = sciezka_zadania
        os.makedirs(os.path.join(self.sciezka_zadnia, "Rozwiązania"), exist_ok=True)
        self.nazwa_pliku = os.path.join("Rozwiązania", "main.py")

    def __str__(self) -> str:
        res = ""
        for linia in self.linie_prototypu:
            if "stworz_zadanie" not in linia and "komenda(" not in linia:
                res += linia
        return res
