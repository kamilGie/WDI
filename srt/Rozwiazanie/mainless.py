from Bazowa import Bazowa


class mainless(Bazowa):
    """Wszystko z prototypu po za mainem"""

    def __str__(self) -> str:
        res = ""
        for linia in self.linie_prototypu:
            if "__name__" in linia:
                return res
            res += linia
        return res
