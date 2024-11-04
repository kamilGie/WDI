import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon69 import longest_increasing_series


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

    def test_Nr01_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 2, 3, 4, 3, 4, 5, 6, 7]), 5)
    def test_Nr02_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1]), 1)
    def test_Nr03_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([2, 4]), 2)
    def test_Nr04_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 3, 5, 7, 9]), 5)
    def test_Nr05_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 2, 4, 6, 8]), 5)
    def test_Nr06_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 1, 1, 1, 1]), 1)
    def test_Nr07_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([10, 8, 6, 4, 2]), 1)
    def test_Nr08_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 2, 3, 1, 2, 3, 4, 2]), 4)
    def test_Nr09_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 2, 3, 5, 6, 7, 9, 10]), 8)
    def test_Nr10_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 5, 3, 7, 9, 11]), 4)
    def test_Nr11_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 3, 5, 7, 2, 4]), 4)
    def test_Nr12_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 2, 4, 8, 16]), 5)
    def test_Nr13_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 1, 1, 2, 3, 4, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4]), 4)
    def test_Nr14_longest_increasing_series_argumenty_tablica(self):
        self.assertEqual(longest_increasing_series([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]), 2)

