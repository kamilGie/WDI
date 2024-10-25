from bazowa import bazowa


class importless(bazowa):
    """
    Wszystko z prototypu po za linijami zawierajacymi `stworz_zadanie` oraz `komenda(`
    """

    def generuj(self):
        res = ""
        for linia in self.linie_prototypu:
            if "stworz_zadanie" not in linia and "komenda(" not in linia:
                res += linia
        return res
