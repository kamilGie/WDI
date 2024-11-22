import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon123 import leng_of_longest_geometric_subsequence


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

    def test_Nr01_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 2, 3, 4, 5]), 1)

    def test_Nr02_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([2, 4, 8, 16, 32]), -1)

    def test_Nr03_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 2, 4, 8, 16]), -1)

    def test_Nr04_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 2, 4, 6, 8]), 1)

    def test_Nr05_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([2, 4, 6, 8, 10]), 1)

    def test_Nr06_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 3, 9, 27, 81]), -1)

    def test_Nr07_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 3, 6, 9, 12]), 1)

    def test_Nr08_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 2, 4, 8, 16, 32]), -1)

    def test_Nr09_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 2, 3, 5, 7]), 1)

    def test_Nr10_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([5, 5, 5, 5, 5]), 0)

    def test_Nr11_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 4, 16, 64, 256]), -1)

    def test_Nr12_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([3, 6, 12, 24, 48, 96]), -1)

    def test_Nr13_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 2, 3]), 1)

    def test_Nr14_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 4, 7]), 1)

    def test_Nr15_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([2, 4, 8, 16, 32]), -1)

    def test_Nr16_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([10, 100, 1000]), -1)

    def test_Nr17_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([1, 3, 6, 9]), 1)

    def test_Nr18_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([0.25, 0.5, 1.0, 2.0, 4.0]), -1)

    def test_Nr19_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([0.5, 1.0, 2.0, 4.0]), -1)

    def test_Nr20_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([0.25, 0.5, 1.5, 3.0, 6.0]), -1)

    def test_Nr21_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([3.33, 6.66, 10, 13.33]), 0)

    def test_Nr22_leng_of_longest_geometric_subsequence_argumenty_tablica(self):
            self.assertEqual(leng_of_longest_geometric_subsequence([3.5, 7.5, 10.5, 14.5]), 0)


