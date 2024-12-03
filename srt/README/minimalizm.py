from Bazowa import Bazowa


from typing import List, Callable


class minimalizm(Bazowa):
    """zawiera tylko tresci oraz kod"""

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
        self.nazwa_pliku = "README.md"

    def parsuj_zadanie(self):
        index_startu = 0
        while self.linie_prototypu[index_startu][0] == "#":
            index_startu += 1

        while self.linie_prototypu[index_startu] == "\n":
            index_startu += 1

        res = "```python\n"
        for linia in self.linie_prototypu[index_startu:]:
            if "__main__" in linia:
                break
            res += linia

        res = res.rstrip("\n")
        res += "```"
        return res

    def __str__(self) -> str:
        res = f"""<picture>
  <source srcset="../../srt/zbior_zadan/{self.nr_zadania}.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_{self.nr_zadania}.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_{self.nr_zadania}.png" alt="zadanie {self.nr_zadania}">
</picture>\n\n"""

        res += self.parsuj_zadanie()

        return res
