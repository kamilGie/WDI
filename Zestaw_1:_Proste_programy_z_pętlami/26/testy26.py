import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon26 import ulamek


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_ulamek_argumenty_1_1_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(1, 1, 1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '1'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_ulamek_argumenty_2_2_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(2, 2, 2)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '1'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_ulamek_argumenty_10_3_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(10, 3, 3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '3.333'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_ulamek_argumenty_10_3_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(10, 3, 10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '3.3333333333'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_ulamek_argumenty_5_2_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(5, 2, 10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '2.5'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_ulamek_argumenty_4_2_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(4, 2, 10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '2'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_ulamek_argumenty_22_7_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(22, 7, 3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '3.142'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_ulamek_argumenty_50_8_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(50, 8, 10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '6.25'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_ulamek_argumenty_100_4_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(100, 4, 10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '25'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_ulamek_argumenty_1_3_50(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(1, 3, 50)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '0.33333333333333333333333333333333333333333333333333'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_ulamek_argumenty_1_6_90(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(1, 6, 90)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '0.166666666666666666666666666666666666666666666666666666666666666666666666666666666666666666'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_ulamek_argumenty_1_9_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(1, 9, 20)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '0.11111111111111111111'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_ulamek_argumenty_0_5_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(0, 5, 100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '0'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_ulamek_argumenty_1_7_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(1, 7, 100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '0.1428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428571428'
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr15_ulamek_argumenty_1_7_2115(self):
        f = io.StringIO()
        with redirect_stdout(f):
            ulamek(1, 7, 2115)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = '0.142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142'
        self.assertEqual(wynik, oczekiwany_wynik)

