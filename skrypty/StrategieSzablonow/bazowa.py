from _utils_S import FunkcjaInput


class Bazowa:
    def __init__(self, linie_prototypu, nr_zadania, funkcje, sciezka_zadania):
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        self.linie_prototypu = linie_prototypu
        self.sciezka = sciezka_zadania
        self.res = ""

    def generuj(self):
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
