from prime import prime

DOKLADNOSCI = int(input("podaj dokładność, z jaką testy mogą zaokrąglać: "))


class float(prime):
    """testy beda zaaokroglac oczekiwany wynik"""

    def metoda_zwracajaca_testow(self, NazwaTestu, numerTestu, zmienne, wynikWywolania):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}(self):
            self.assertAlmostEqual({NazwaTestu}({zmienne}), { wynikWywolania }, places={DOKLADNOSCI})\n"""

    def metoda_nasluchujaca_testow(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({zmienne})
            wynik = f.getvalue().strip()

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""
