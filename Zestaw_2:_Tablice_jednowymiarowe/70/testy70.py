import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon70 import longest_geometric_series


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

    def test_Nr01_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([1, 2, 4]), 3)
    def test_Nr02_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([1, 1, 1, 1, 1]), 5)
    def test_Nr03_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2]), 1)
    def test_Nr04_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([]), 0)
    def test_Nr05_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([3, 9]), 2)
    def test_Nr06_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 4, 8, 16]), 4)
    def test_Nr07_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 4, 8, 2, 4, 8]), 3)
    def test_Nr08_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 3, 5, 7, 11]), 2)
    def test_Nr09_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([1, 2, 4, 8, 16]), 5)
    def test_Nr10_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([3, 9, 27, 2, 6]), 3)
    def test_Nr11_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 6, 18, 54]), 4)
    def test_Nr12_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([1, 3, 9, 18, 36]), 3)
    def test_Nr13_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 3, 4, 5, 6]), 2)
    def test_Nr14_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 4, 8, 16, 3, 9, 27, 81, 1, 3, 9, 27]), 4)
    def test_Nr15_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 3, 5, 7, 11, 13, 17]), 2)
    def test_Nr16_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([5, 10, 20, 40, 2, 4, 8, 16]), 4)
    def test_Nr17_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 6, 18, 54, 1, 3, 9, 27, 81]), 5)
    def test_Nr18_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([2, 2, 2, 4, 8, 16, 3, 3, 3]), 4)
    def test_Nr19_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([1, 2, 4, 8, 16, 1, 1, 1, 1]), 5)
    def test_Nr20_longest_geometric_series_argumenty_tablica(self):
        self.assertEqual(longest_geometric_series([1, 2, 4, 8, 2, 6, 18, 54, 1, 2, 4]), 4)

