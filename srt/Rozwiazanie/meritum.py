import inspect
from Bazowa import Bazowa


class meritum(Bazowa):
    """Sama funkcja przekazana"""

    def __str__(self) -> str:
        res = ""
        for funkcja in self.funkcje:
            res += inspect.getsource(funkcja)
            res += "\n"
        return res
