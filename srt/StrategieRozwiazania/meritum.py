from bazowa import bazowa
import inspect


class meritum(bazowa):
    def generuj(self):
        res = ""
        for funkcja in self.funkcje:
            res += inspect.getsource(funkcja)
            res += "\n"
        return res
