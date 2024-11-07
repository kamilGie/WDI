from prime import prime

DOKLADNOSCI = int(input("podaj dokładność, z jaką testy mogą zaokrąglać: "))


class float(prime):
    """testy beda zaaokroglac oczekiwany wynik"""

    def metoda_zwracajaca_testow_bez_kolejnosci(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            wynik  = {NazwaTestu}({', '.join(map(str, zmienne))})

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""

    def metoda_nasluchujaca_testow_bez_kolejnosci(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""
