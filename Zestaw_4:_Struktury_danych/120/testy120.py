import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon120 import skr, add, subtract, mult, div, exp


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

    def test_Nr01_skr_argumenty_tablica(self):
            self.assertEqual(skr([1, 1]), (1, 1))

    def test_Nr02_skr_argumenty_tablica(self):
            self.assertEqual(skr([2, 2]), (1, 1))

    def test_Nr03_skr_argumenty_tablica(self):
            self.assertEqual(skr([8, 4]), (2, 1))

    def test_Nr04_skr_argumenty_tablica(self):
            self.assertEqual(skr([6, 4]), (3, 2))

    def test_Nr05_skr_argumenty_tablica(self):
            self.assertEqual(skr([10, 100]), (1, 10))

    def test_Nr06_skr_argumenty_tablica(self):
            self.assertEqual(skr([12312, 12312]), (1, 1))

    def test_Nr07_skr_argumenty_tablica(self):
            self.assertEqual(skr([12, 31]), (12, 31))

    def test_Nr08_skr_argumenty_tablica(self):
            self.assertEqual(skr([4123, 3223]), (4123, 3223))

    def test_Nr09_skr_argumenty_tablica(self):
            self.assertEqual(skr([12345, 12540]), (823, 836))

    def test_Nr01_add_argumenty_tablica_tablica(self):
            self.assertEqual(add([1, 1], [2, 2]), (2, 1))

    def test_Nr02_add_argumenty_tablica_tablica(self):
            self.assertEqual(add([3, 3], [5, 5]), (2, 1))

    def test_Nr03_add_argumenty_tablica_tablica(self):
            self.assertEqual(add([123, 412], [12, 23]), (7773, 9476))

    def test_Nr04_add_argumenty_tablica_tablica(self):
            self.assertEqual(add([12, 1], [11, 41]), (503, 41))

    def test_Nr05_add_argumenty_tablica_tablica(self):
            self.assertEqual(add([2, 2], [2, 2]), (2, 1))

    def test_Nr06_add_argumenty_tablica_tablica(self):
            self.assertEqual(add([4, 2], [8, 4]), (4, 1))

    def test_Nr01_subtract_argumenty_tablica_tablica(self):
            self.assertEqual(subtract([2, 1], [1, 1]), (1, 1))

    def test_Nr02_subtract_argumenty_tablica_tablica(self):
            self.assertEqual(subtract([4, 2], [8, 4]), (0, 1))

    def test_Nr03_subtract_argumenty_tablica_tablica(self):
            self.assertEqual(subtract([12345, 5], [120, 2]), (2409, 1))

    def test_Nr04_subtract_argumenty_tablica_tablica(self):
            self.assertEqual(subtract([2115, 5], [100, 2]), (373, 1))

    def test_Nr05_subtract_argumenty_tablica_tablica(self):
            self.assertEqual(subtract([1234, 23], [23, 4231]), (5220525, 97313))

    def test_Nr01_mult_argumenty_tablica_tablica(self):
            self.assertEqual(mult([2, 1], [2, 1]), (4, 1))

    def test_Nr02_mult_argumenty_tablica_tablica(self):
            self.assertEqual(mult([4, 2], [14, 12]), (7, 3))

    def test_Nr03_mult_argumenty_tablica_tablica(self):
            self.assertEqual(mult([214, 1], [123, 323]), (26322, 323))

    def test_Nr04_mult_argumenty_tablica_tablica(self):
            self.assertEqual(mult([1, 2], [23, 1]), (23, 2))

    def test_Nr05_mult_argumenty_tablica_tablica(self):
            self.assertEqual(mult([321, 412], [123, 5]), (39483, 2060))

    def test_Nr06_mult_argumenty_tablica_tablica(self):
            self.assertEqual(mult([1, 1], [1, 1]), (1, 1))

    def test_Nr01_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([4, 2], [2, 1]), (1, 1))

    def test_Nr02_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([10, 1], [123, 123]), (10, 1))

    def test_Nr03_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([11, 1], [231, 2]), (2, 21))

    def test_Nr04_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([2312, 2], [123, 123]), (1156, 1))

    def test_Nr05_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([1231, 1231], [123145, 123]), (123, 123145))

    def test_Nr06_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([23, 1232], [123, 3]), (23, 50512))

    def test_Nr07_div_argumenty_tablica_tablica(self):
            self.assertEqual(div([213, 512], [123, 512]), (71, 41))

    def test_Nr01_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([2, 2], [2, 2]), (1.0, 1.0))

    def test_Nr02_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([2, 1], [2, 1]), (4.0, 1.0))

    def test_Nr03_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([4, 3], [4, 3]), (6.3496042078727974, 4.3267487109222245))

    def test_Nr04_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([51, 12], [123, 123]), (17.000000000000004, 4.000000000000001))

    def test_Nr05_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([231, 123], [123, 1]), (1.0923434181681859e+232, 2.3572973963943497e+198))

    def test_Nr06_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([23, 1], [23, 5]), (1836318.652801944, 1.0))

    def test_Nr07_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([4, 1], [1, 2]), (2.0, 1.0))

    def test_Nr08_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([123, 41], [12, 1]), (531441.0, 1.0))

    def test_Nr09_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([31, 12], [123, 5]), (4.869649107005086e+36, 3.530682400810842e+26))

    def test_Nr10_exp_argumenty_tablica_tablica(self):
            self.assertEqual(exp([123, 23], [5, 2]), (167788.72680546806, 2536.9948758324285))


