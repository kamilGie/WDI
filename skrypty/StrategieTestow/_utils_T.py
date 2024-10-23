RAMKA = "# ====================================================================================================>\n"


def GoraKlasyTestow(nr_zadania, funkcje):
    funkcjeStr = ", ".join(funkcja.__name__ for funkcja in funkcje)
    return f"""import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon{nr_zadania} import {funkcjeStr}


def komenda(k: str, *args, **kwargs):
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    skrypty_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty")
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class Testy{nr_zadania}:
    class testy(unittest.TestCase):
"""


def MetodaKlasyTestow(NazwaTestu, numerTestu, zmienne, wynikWywolania):
    return f"""\n
        def test_Nr{numerTestu}_{NazwaTestu}_parametry_{'_'.join(map(str, zmienne))}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            oczekiwany_wynik = [{ wynikWywolania }]
            self.assertIn(wynik, oczekiwany_wynik)"""


def DolKlasyTestow(nrZadania):
    return f"""
    @staticmethod
    def Uruchom():
        suite = unittest.TestLoader().loadTestsFromTestCase(Testy{nrZadania}.testy)
        unittest.TextTestRunner(verbosity=2).run(suite)"""
