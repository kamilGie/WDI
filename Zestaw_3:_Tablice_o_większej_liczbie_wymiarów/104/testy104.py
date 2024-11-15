import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon104 import Zadanie_104


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

    def test_Nr01_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[1, 2], [2, 3]]), [[1, 2], [2, 3]])

    def test_Nr02_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[4, 5, 6], [7, 8, 9], [10, 11, 12]]), [[4, 5, 6], [7, 8, 9], [10, 11, 12]])

    def test_Nr03_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[13, 1], [2, 7]]), [[0, 1], [2, 0]])

    def test_Nr04_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[2, 3, 5], [6, 7, 11], [13, 17, 19]]), [[2, 3, 5], [6, 7, 11], [13, 17, 0]])

    def test_Nr05_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[1, 8, 4], [2, 3, 9], [10, 5, 7]]), [[1, 8, 4], [2, 3, 9], [10, 5, 7]])

    def test_Nr06_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[1, 8, 4], [2, 3, 9], [10, 5, 7]]), [[1, 8, 4], [2, 3, 9], [10, 5, 7]])

    def test_Nr07_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]), [[3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

    def test_Nr08_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[2, 5, 7], [4, 11, 6], [3, 8, 9]]), [[2, 5, 7], [4, 11, 6], [3, 8, 9]])

    def test_Nr09_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[10, 4, 6, 3], [7, 9, 8, 12], [2, 5, 4, 6], [15, 13, 2, 8]]), [[10, 4, 6, 3], [7, 9, 8, 12], [2, 5, 4, 6], [15, 13, 2, 8]])

    def test_Nr10_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[6, 2, 9, 3], [7, 10, 12, 5], [11, 13, 17, 19], [2, 5, 8, 4]]), [[6, 2, 9, 3], [7, 10, 12, 5], [11, 13, 17, 19], [2, 5, 8, 4]])

    def test_Nr11_Zadanie_104_argumenty_tablica(self):
            self.assertEqual(Zadanie_104([[4, 5], [1, 10]]), [[4, 0], [1, 10]])


