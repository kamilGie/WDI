from bazowa import bazowa
from _utils_S import funkcja_input, main, parsuj_prototyp


class domyslna(bazowa):
    def generuj(self):
        self.res = parsuj_prototyp(self.linie_prototypu, self.funkcje)

        cialo_maina = "\n"
        for funkcja in self.funkcje:
            cialo_maina += funkcja_input(funkcja)
        self.res += main(self.nr_zadania, cialo_maina)
