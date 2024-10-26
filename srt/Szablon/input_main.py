from Bazowa import Bazowa

from _utils_S import funkcja_input, main, parsuj_prototyp


class input_main(Bazowa):
    def __str__(self) -> str:
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje)

        cialo_maina = "\n"
        for funkcja in self.funkcje:
            cialo_maina += funkcja_input(funkcja)
        res += main(self.nr_zadania, cialo_maina)
        return res
