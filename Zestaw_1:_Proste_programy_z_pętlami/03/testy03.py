import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon03 import Zadanie_3


def komenda(k: str, *args, **kwargs):
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    skrypty_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty")
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class Testy03:
    class testy(unittest.TestCase):


        def test_Nr1_Zadanie_3_parametry_(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_3()
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['(19, 11)']
            self.assertIn(wynik, oczekiwany_wynik)

    @staticmethod
    def Uruchom():
        suite = unittest.TestLoader().loadTestsFromTestCase(Testy03.testy)
        unittest.TextTestRunner(verbosity=2).run(suite)