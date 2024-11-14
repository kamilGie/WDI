import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon108 import Zadanie_108


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

    def test_Nr01_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (1, 1))

    def test_Nr02_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[1, 1, 1], [1, 5, 1], [1, 1, 1]]), (0, 1))

    def test_Nr03_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[3, 3, 3], [3, 9, 3], [3, 3, 3]]), (1, 1))

    def test_Nr04_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), (1, 1))

    def test_Nr05_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[9, 2, 5], [3, 5, 1], [8, 0, 7]]), (1, 1))

    def test_Nr06_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[1, 1], [1, 1]]), (0, 0))

    def test_Nr07_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]), (1, 1))

    def test_Nr08_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), (2, 2))

    def test_Nr09_Zadanie_108_argumenty_tablica(self):
            self.assertEqual(Zadanie_108([[0, 1, 0], [1, 0, 1], [0, 1, 0]]), (1, 1))


