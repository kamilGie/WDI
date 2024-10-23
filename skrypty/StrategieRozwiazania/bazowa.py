class Bazowa:
    def __init__(self, linie_prototypu, nr_zadania, funkcje, sciezka_zadania):
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka = sciezka_zadania
        self.res = ""

    def generuj(self):
        for linia in self.linie_prototypu:
            if "stworz_zadanie" not in linia:
                self.res += linia
