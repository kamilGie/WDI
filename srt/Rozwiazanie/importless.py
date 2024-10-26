from Bazowa import Bazowa


class importless(Bazowa):
    """Wszystko z prototypu po za linijami zawierajacymi `stworz_zadanie` oraz `komenda(`"""

    def __str__(self) -> str:
        res = ""
        for linia in self.linie_prototypu:
            if "stworz_zadanie" not in linia and "komenda(" not in linia:
                res += linia
        return res
