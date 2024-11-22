import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon145 import Zadanie_145


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_145_argumenty_tablica_12_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 6, 12], 12, 2)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[3, 4]\n[2, 6]\n[1, 12]")

    def test_Nr02_Zadanie_145_argumenty_tablica_12_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 6, 12], 12, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[1, 3, 4]\n[1, 2, 6]")

    def test_Nr03_Zadanie_145_argumenty_tablica_24_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 6, 12], 24, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 4]\n[1, 4, 6]\n[1, 2, 12]")

    def test_Nr04_Zadanie_145_argumenty_tablica_48_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 6, 12, 8], 48, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 4, 6]\n[2, 3, 8]\n[1, 6, 8]\n[1, 4, 12]")

    def test_Nr05_Zadanie_145_argumenty_tablica_128_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 6, 12, 8, 16], 128, 4)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[1, 2, 4, 16]")

    def test_Nr06_Zadanie_145_argumenty_tablica_64_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 4, 8, 16], 64, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 4, 8]")

    def test_Nr07_Zadanie_145_argumenty_tablica_15_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 3, 5, 7, 11], 15, 2)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[3, 5]")

    def test_Nr08_Zadanie_145_argumenty_tablica_1_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 6, 12], 1, 1)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[1]")

    def test_Nr09_Zadanie_145_argumenty_tablica_30_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 3, 5, 7, 11], 30, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 5]")

    def test_Nr10_Zadanie_145_argumenty_tablica_1_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 1, 1, 1, 1], 1, 5)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[1, 1, 1, 1, 1]")

    def test_Nr11_Zadanie_145_argumenty_tablica_2_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 1, 1, 1, 1, 2], 2, 6)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[1, 1, 1, 1, 1, 2]")

    def test_Nr12_Zadanie_145_argumenty_tablica_30_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 3, 5, 10, 15, 30], 30, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 5]")

    def test_Nr13_Zadanie_145_argumenty_tablica_16_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 2, 2, 2], 16, 4)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 2, 2, 2]")

    def test_Nr15_Zadanie_145_argumenty_tablica_60_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 5, 6], 60, 4)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[1, 3, 4, 5]\n[1, 2, 5, 6]")

    def test_Nr16_Zadanie_145_argumenty_tablica_36_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 5, 6, 7, 8, 9], 36, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 6]\n[1, 4, 9]")

    def test_Nr17_Zadanie_145_argumenty_tablica_20_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 4, 6, 8, 10], 20, 2)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 10]")

    def test_Nr18_Zadanie_145_argumenty_tablica_210_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([2, 3, 5, 7, 11, 13, 17], 210, 4)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 5, 7]")

    def test_Nr19_Zadanie_145_argumenty_tablica_45_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 3, 5, 7, 9, 11, 13, 15], 45, 2)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[5, 9]\n[3, 15]")

    def test_Nr20_Zadanie_145_argumenty_tablica_315_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([3, 5, 7, 9, 11, 13, 15], 315, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[5, 7, 9]\n[3, 7, 15]")

    def test_Nr21_Zadanie_145_argumenty_tablica_42_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_145([1, 2, 3, 4, 5, 6, 7], 42, 3)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 7]\n[1, 6, 7]")
