import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon093 import only_odd_in_verses


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

    def test_Nr01_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[11, 33, 77], [13, 35, 99], [111, 55, 93]]), True)

    def test_Nr02_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[12, 34, 77], [22, 33, 44], [101, 55, 90]]), True)

    def test_Nr03_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[12, 34, 78], [13, 35, 99], [21, 44, 56]]), False)

    def test_Nr04_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[1, 2, 3], [4, 5, 7], [9, 6, 8]]), False)

    def test_Nr05_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[11, 23, 19], [3, 15, 7], [101, 33, 55]]), False)

    def test_Nr06_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[1234, 567, 999], [234, 789, 555], [222, 444, 999]]), True)

    def test_Nr07_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([]), True)

    def test_Nr08_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), False)

    def test_Nr09_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[1]]), True)

    def test_Nr10_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[15, 28, 37], [55, 44, 93], [99, 101, 111]]), True)

    def test_Nr11_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[888, 44, 222], [666, 444, 888], [222, 888, 444]]), False)

    def test_Nr12_only_odd_in_verses_argumenty_tablica(self):
            self.assertEqual(only_odd_in_verses([[13, 57, 92], [35, 92, 71], [101, 22, 11]]), False)


