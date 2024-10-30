import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon82 import n_liczba_z_pierwiastka_z_2


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

    def test_Nr01_n_liczba_z_pierwiastka_z_2_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_n_liczba_z_pierwiastka_z_2_argumenty_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(5)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_n_liczba_z_pierwiastka_z_2_argumenty_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_n_liczba_z_pierwiastka_z_2_argumenty_12(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(12)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_n_liczba_z_pierwiastka_z_2_argumenty_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(20)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 9
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_n_liczba_z_pierwiastka_z_2_argumenty_32(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(32)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 9
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_n_liczba_z_pierwiastka_z_2_argumenty_39(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(39)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 9
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_n_liczba_z_pierwiastka_z_2_argumenty_50(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(50)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 9
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_n_liczba_z_pierwiastka_z_2_argumenty_59(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(59)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 7
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_n_liczba_z_pierwiastka_z_2_argumenty_69(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(69)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_n_liczba_z_pierwiastka_z_2_argumenty_79(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(79)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_n_liczba_z_pierwiastka_z_2_argumenty_89(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(89)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_n_liczba_z_pierwiastka_z_2_argumenty_91(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(91)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_n_liczba_z_pierwiastka_z_2_argumenty_96(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(96)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr15_n_liczba_z_pierwiastka_z_2_argumenty_99(self):
        f = io.StringIO()
        with redirect_stdout(f):
            n_liczba_z_pierwiastka_z_2(99)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)

