import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon109 import Zadanie_109


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

    def test_Nr01_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_Nr02_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), 58)

    def test_Nr03_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 3)

    def test_Nr04_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[5, 5, 5, 5], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]), 20)

    def test_Nr05_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[10, -20, 30], [5, -15, 25], [40, -50, 60]]), 115)

    def test_Nr06_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[-1, 2, -3], [-4, 5, -6], [7, -8, 9]]), 8)

    def test_Nr07_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[-1, 2, 3], [-4, -5, 6], [7, 8, 9]]), 24)

    def test_Nr08_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [-16, 17, -18, 19, 20], [21, -22, 23, -24, 25]]), 70)

    def test_Nr09_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[10, -2, 3, -4, 5, 6, -7, 8], [-9, 10, -11, 12, -13, 14, -15, 16], [17, -18, 19, -20, 21, 22, 23, -24], [25, 26, -27, 28, 29, -30, 31, 32], [-33, 34, 35, -36, 37, 38, 39, 40], [41, -42, 43, 44, -45, 46, 47, 48], [-49, 50, 51, 52, -53, 54, 55, 56], [57, -58, 59, 60, 61, 62, 63, -64]]), 305)

    def test_Nr10_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[3, -2, 1, 4, 5], [6, -1, 2, -3, 4], [-5, 6, 7, -8, 9], [10, -11, 12, 13, 14], [-15, 16, -17, 18, 19]]), 51)

    def test_Nr11_Zadanie_109_argumenty_tablica(self):
            self.assertEqual(Zadanie_109([[2115, 1410], [2115, 2004]]), 4230)


