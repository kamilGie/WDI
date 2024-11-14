import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon111 import Zadanie_111


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

    def test_Nr01_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), ([2, 2], [3, 3]))

    def test_Nr02_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[100, 2, 3, 4], [5, 6, 7, 100], [9, 100, 11, 12], [13, 14, 15, 100]]), ([1, 0], [2, 3]))

    def test_Nr03_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[0, 0, 0, 0], [0, 99, 0, 0], [0, 0, 0, 0], [0, 0, 0, 99]]), ([0, 1], [1, 3]))

    def test_Nr04_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]]), ([2, 2], [3, 3]))

    def test_Nr05_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[5, 3, 1, 2], [8, 7, 4, 6], [9, 2, 3, 5], [1, 4, 6, 8]]), ([1, 0], [2, 3]))

    def test_Nr06_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]), ([2, 2], [3, 3]))

    def test_Nr07_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[10, 15, 20, 25], [30, 35, 40, 45], [50, 55, 60, 65], [70, 75, 80, 85]]), ([2, 2], [3, 3]))

    def test_Nr08_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[1, 0, 0, 1], [0, 2, 2, 0], [1, 3, 3, 1], [0, 0, 1, 0]]), ([0, 1], [2, 2]))

    def test_Nr09_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[99, 1, 1, 99], [1, 50, 50, 1], [1, 1, 99, 99], [99, 1, 1, 99]]), ([2, 0], [3, 3]))

    def test_Nr10_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[1000, 2000, 3000, 4000], [5000, 6000, 7000, 8000], [9000, 10000, 11000, 12000], [13000, 14000, 15000, 16000]]), ([2, 2], [3, 3]))

    def test_Nr11_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[3, 5, 2, 6], [7, 1, 9, 4], [8, 6, 3, 5], [4, 9, 7, 1]]), ([1, 1], [2, 2]))

    def test_Nr12_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[10, 20, 10, 20], [30, 40, 30, 40], [50, 60, 50, 60], [70, 80, 70, 80]]), ([2, 1], [3, 3]))

    def test_Nr13_Zadanie_111_argumenty_tablica(self):
            self.assertEqual(Zadanie_111([[100, 200, 300, 400], [400, 300, 200, 100], [100, 200, 300, 400], [400, 300, 200, 100]]), ([0, 0], [1, 3]))


