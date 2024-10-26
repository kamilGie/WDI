import inspect
from Bazowa import Bazowa


class meritum(Bazowa):
    def generuj(self):
        res = ""
        for funkcja in self.funkcje:
            res += inspect.getsource(funkcja)
            res += "\n"
        return res
