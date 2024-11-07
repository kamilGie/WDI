from _utils_S import main, parsuj_prototyp
from Bazowa import Bazowa


class zwykle(Bazowa):
    def __str__(self) -> str:
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
