import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon119 import Zadanie_119


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

    def test_Nr01_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 1], [2, 2, 3], [4, 4, 4]]), 0)

    def test_Nr02_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 2], [3, 3, 3], [4, 4, 4]]), 1)

    def test_Nr03_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 1], [1, 2, 3], [3, 3, 3]]), 0)

    def test_Nr04_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 1, 2], [3, 3, 3, 4], [5, 5, 5, 5], [6, 7, 7, 7]]), 2)

    def test_Nr05_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 2, 3, 4, 5], [1, 2, 2, 2, 3], [4, 4, 5, 6, 6], [7, 7, 8, 9, 9], [1, 1, 1, 1, 1]]), 4)

    def test_Nr06_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 1, 1, 1], [1, 1, 1, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]), 0)

    def test_Nr07_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 1, 1], [1, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]), 0)

    def test_Nr08_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 2, 3, 4], [1, 2, 3, 4], [5, 6, 7, 8], [9, 9, 9, 9]]), 3)

    def test_Nr09_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[10, 10, 10, 10, 10], [10, 11, 11, 11, 10], [12, 12, 12, 12, 10], [13, 13, 13, 13, 10], [14, 14, 14, 14, 10]]), 0)

    def test_Nr10_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [7, 7, 7, 8, 8, 8], [9, 9, 9, 9, 9, 9], [10, 10, 10, 11, 11, 11], [12, 12, 12, 12, 12, 12]]), 3)

    def test_Nr11_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[1, 1, 2], [2, 3, 3], [3, 4, 4]]), 0)

    def test_Nr12_Zadanie_119_argumenty_tablica(self):
            self.assertEqual(Zadanie_119([[5, 5, 5, 5], [5, 5, 5, 6], [6, 6, 6, 6], [7, 7, 7, 7]]), 0)


