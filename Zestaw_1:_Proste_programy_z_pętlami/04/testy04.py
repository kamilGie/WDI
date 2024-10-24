import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon04 import is_in_fib


def komenda(k: str, *args, **kwargs):
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    skrypty_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty")
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class Testy04:
    class testy(unittest.TestCase):


        def test_Nr1_is_in_fib_parametry_1(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(1)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['True']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr2_is_in_fib_parametry_10(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(10)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['True']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr3_is_in_fib_parametry_200(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(200)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr4_is_in_fib_parametry_891(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(891)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr5_is_in_fib_parametry_431(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(431)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr6_is_in_fib_parametry_500(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(500)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr7_is_in_fib_parametry_0(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(0)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['True']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr8_is_in_fib_parametry_234234(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(234234)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr9_is_in_fib_parametry_93827984723(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(93827984723)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr10_is_in_fib_parametry_331(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(331)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

        def test_Nr11_is_in_fib_parametry_891(self):
            f = io.StringIO()
            with redirect_stdout(f):
                is_in_fib(891)
            wynik = f.getvalue().strip()

            oczekiwany_wynik = ['False']
            self.assertIn(wynik, oczekiwany_wynik)

    @staticmethod
    def Uruchom():
        suite = unittest.TestLoader().loadTestsFromTestCase(Testy04.testy)
        unittest.TextTestRunner(verbosity=2).run(suite)