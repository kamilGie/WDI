import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon76 import maska_tritowa


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

    def test_Nr01_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 2], [3, 5]), 3)

    def test_Nr02_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1], [1]), 1)

    def test_Nr03_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([2, 3], [5, 7]), 2)

    def test_Nr04_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([4, 6], [8, 10]), 0)

    def test_Nr05_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([3], [5]), 2)

    def test_Nr06_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 4, 2], [6, 7, 3]), 10)

    def test_Nr07_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 2, 5, 4], [3, 7, 9, 2]), 24)

    def test_Nr08_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([0, 2, 1], [0, 7, 3]), 12)

    def test_Nr09_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 3, 2, 4], [9, 7, 4, 8]), 17)

    def test_Nr10_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 4], [3, 5]), 3)

    def test_Nr11_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 0], [0, 6]), 4)

    def test_Nr12_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([1, 4, 52, 3, 5, 2, 35], [33, 0, 93, 5, 12, 2, 5]), 410)

    def test_Nr13_maska_tritowa_argumenty_tablica_tablica(self):
            self.assertEqual(maska_tritowa([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)


