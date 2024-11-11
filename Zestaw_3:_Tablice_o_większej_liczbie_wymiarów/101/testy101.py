import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon101 import Zadanie_101


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

    def test_Nr01_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1], [1, 0]]), True)

    def test_Nr02_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2], [3, 0, 4], [5, 6, 0]]), True)

    def test_Nr03_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[1, 2], [3, 4]]), False)

    def test_Nr04_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2], [0, 3, 4], [5, 6, 7]]), False)

    def test_Nr05_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2], [0, 0, 0], [5, 6, 7]]), False)

    def test_Nr06_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 7], [0, 8, 9, 10]]), False)

    def test_Nr07_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2], [3, 0, 4], [5, 6, 0]]), True)

    def test_Nr08_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 7], [0, 8, 9, 10]]), False)

    def test_Nr09_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[1, 2, 3], [0, 4, 5], [6, 7, 0]]), False)

    def test_Nr10_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2], [3, 0, 4]]), True)

    def test_Nr11_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2, 3], [4, 0, 5, 6], [7, 8, 0, 9], [10, 11, 12, 0]]), True)

    def test_Nr12_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0]]), True)

    def test_Nr13_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[1]]), False)

    def test_Nr14_Zadanie_101_argumenty_tablica(self):
            self.assertEqual(Zadanie_101([[0, 1, 2], [1, 0, 3], [4, 5, 0]]), True)


