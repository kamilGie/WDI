import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon143 import Zadanie_143


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

    def test_Nr01_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 1, 0], [1, 0, 1], [1, -1, -1]]), 3)

    def test_Nr02_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), 0)

    def test_Nr03_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 2], [3, 4]]), -2)

    def test_Nr04_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 1)

    def test_Nr05_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2, 4, 1], [3, 2, 5], [1, 3, 4]]), -35)

    def test_Nr06_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[5, 0, 1], [2, 3, 4], [1, 5, 6]]), -3)

    def test_Nr07_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 0)

    def test_Nr08_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 2], [0, 3]]), 3)

    def test_Nr09_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2, 5, 6], [1, 4, 2], [7, 8, 9]]), -55)

    def test_Nr10_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 2, 3], [0, 1, 4], [2, 1, 1]]), 7)

    def test_Nr11_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[0, 1, 2], [3, 1, 0], [4, 5, 6]]), 4)

    def test_Nr12_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[7, 8, 9], [4, 5, 6], [1, 2, 3]]), 0)

    def test_Nr13_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 1, 1], [0, 0, 0], [1, 1, 1]]), 0)

    def test_Nr14_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[3, 2, 1], [5, 6, 7], [9, 8, 7]]), 0)

    def test_Nr15_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 3], [2, 4]]), -2)

    def test_Nr16_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[4, 5, 6, 7], [2, 3, 1, 6], [8, 7, 9, 4], [5, 6, 2, 1]]), 260)

    def test_Nr17_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[100, 200, 300, 400], [500, 600, 700, 800], [900, 1000, 1100, 1200], [1300, 1400, 1500, 1600]]), 0)

    def test_Nr18_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]]), 0)

    def test_Nr19_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [32, 34, 36, 38, 40], [42, 44, 46, 48, 50]]), 0)

    def test_Nr20_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 32, 33, 34, 35]]), 0)

    def test_Nr21_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]), 0)

    def test_Nr22_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [32, 34, 36, 38, 40], [42, 44, 46, 48, 50]]), 0)

    def test_Nr23_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2, 4, 6, 8, 10], [12, 0, 16, 18, 20], [22, 24, 26, 1, 30], [32, 3, 36, 38, 40], [42, 44, 46, 9, 50]]), 0)

    def test_Nr24_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2, 4, 6, 8, 0], [12, 0, 16, 18, 20], [22, 24, 26, 1, 30], [32, 3, 36, 38, 40], [42, 44, 46, 9, 50]]), 151200)

    def test_Nr25_Zadanie_143_argumenty_tablica(self):
            self.assertEqual(Zadanie_143([[2115]]), 2115)


