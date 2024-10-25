from bazowa import bazowa


class domyslna(bazowa):
    """
    Wszystko z prototypu po za linijami zawierajacymi `stworz_zadanie` oraz `komenda(`
    """

    def generuj(self):
        for linia in self.linie_prototypu:
            if "stworz_zadanie" not in linia and "komenda(" not in linia:
                self.res += linia
