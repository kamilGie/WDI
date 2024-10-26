import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon05 import Zadanie_5


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_Zadanie_5_argumenty_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['0']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr2_Zadanie_5_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['1']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr3_Zadanie_5_argumenty_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(2)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['1']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr4_Zadanie_5_argumenty_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(4)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['2']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr5_Zadanie_5_argumenty_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(8)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['2']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr6_Zadanie_5_argumenty_9(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(9)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['3']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr7_Zadanie_5_argumenty_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(20)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['4']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr8_Zadanie_5_argumenty_26(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(26)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['5']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr9_Zadanie_5_argumenty_81(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(81)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['9']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_5_argumenty_12345(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(12345)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['111']
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_5_argumenty_123123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(123123)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ['350']
        self.assertIn(wynik, oczekiwany_wynik)

