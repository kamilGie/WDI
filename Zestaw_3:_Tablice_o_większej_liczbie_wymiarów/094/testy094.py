import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon094 import check_tab_for_even_verses


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

    def test_Nr01_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[12, 34, 56], [78, 90, 22], [44, 66, 88]]), True)

    def test_Nr02_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[11, 33, 57], [78, 90, 22], [13, 55, 93]]), True)

    def test_Nr03_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[11, 33, 57], [13, 55, 93], [19, 31, 53]]), False)

    def test_Nr04_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[1, 3, 5], [2, 4, 6], [7, 9, 11]]), True)

    def test_Nr05_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[123, 135, 137], [246, 357, 246], [753, 951, 357]]), False)

    def test_Nr06_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[13, 35, 79], [13, 35, 97], [111, 333, 555]]), False)

    def test_Nr07_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[246, 482, 864], [135, 357, 135], [777, 975, 555]]), True)

    def test_Nr08_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[222, 444, 666], [888, 246, 468], [680, 802, 246]]), True)

    def test_Nr09_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[111, 333, 555], [777, 111, 333], [135, 357, 579]]), False)

    def test_Nr10_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[20, 31, 42], [19, 23, 57], [53, 75, 31]]), False)

    def test_Nr11_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[9, 21, 53], [43, 55, 67], [89, 13, 17]]), False)

    def test_Nr12_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[222, 444, 555], [666, 777, 888], [999, 111, 333]]), False)

    def test_Nr13_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), True)

    def test_Nr14_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[11, 33, 55], [77, 99, 113], [131, 151, 173]]), False)

    def test_Nr15_check_tab_for_even_verses_argumenty_tablica(self):
            self.assertEqual(check_tab_for_even_verses([[102, 203, 307], [409, 511, 611], [702, 803, 904]]), True)


