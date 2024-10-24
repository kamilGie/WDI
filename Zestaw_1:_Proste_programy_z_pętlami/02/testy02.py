import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon02 import Zadanie_2


def komenda(k: str, *args, **kwargs):
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    skrypty_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty")
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class Testy02:
    class testy(unittest.TestCase):


        def test_Nr1_Zadanie_2_parametry_(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_2()
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n89\n144\n233\n377\n610\n987\n1597\n2584\n4181\n6765\n10946\n17711\n28657\n46368\n75025\n121393\n196418\n317811\n514229\n832040']
            self.assertIn(wynik, oczekiwany_wynik)

    @staticmethod
    def Uruchom():
        suite = unittest.TestLoader().loadTestsFromTestCase(Testy02.testy)
        unittest.TextTestRunner(verbosity=2).run(suite)