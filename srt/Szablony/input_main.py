from Bazowa import Bazowa

print("kurwa")
from _utils_S import funkcja_input, main, parsuj_prototyp


class input_main(Bazowa):
    def generuj(self):
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje)

        cialo_maina = "\n"
        for funkcja in self.funkcje:
            cialo_maina += funkcja_input(funkcja)
        res += main(self.nr_zadania, cialo_maina)
        print(res)
        return res
