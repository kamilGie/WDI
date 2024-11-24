import unittest
import os
import sys
import importlib

from szablon125 import dodawanie, odejmowanie, mnozenie, dzielenie, potegowanie


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_dodawanie_argumenty_tablica_tablica(self):
        self.assertEqual(dodawanie([1, 2], [3, 4]), (4, 6))

    def test_Nr02_dodawanie_argumenty_tablica_tablica(self):
        self.assertEqual(dodawanie([0, 0], [0, 0]), (0, 0))

    def test_Nr03_dodawanie_argumenty_tablica_tablica(self):
        self.assertEqual(dodawanie([-1, -1], [1, 1]), (0, 0))

    def test_Nr04_dodawanie_argumenty_tablica_tablica(self):
        self.assertEqual(dodawanie([5, 3], [2, -2]), (7, 1))

    def test_Nr05_dodawanie_argumenty_tablica_tablica(self):
        self.assertEqual(dodawanie([10, 15], [-10, -5]), (0, 10))

    def test_Nr01_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([5, 7], [3, 2]), (2, 5))

    def test_Nr02_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([0, 0], [0, 0]), (0, 0))

    def test_Nr03_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([-1, -1], [1, 1]), (-2, -2))

    def test_Nr04_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([10, 5], [5, 10]), (5, -5))

    def test_Nr05_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([3, 4], [-3, -4]), (6, 8))

    def test_Nr06_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([0, 0], [3, 4]), (-3, -4))

    def test_Nr07_odejmowanie_argumenty_tablica_tablica(self):
        self.assertEqual(odejmowanie([0, 0], [-3, -4]), (3, 4))

    def test_Nr01_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([1, 1], [1, -1]), (2, 0))

    def test_Nr02_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([0, 0], [1, 1]), (0, 0))

    def test_Nr03_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([-1, -1], [1, 1]), (0, -2))

    def test_Nr04_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([3, 4], [5, -6]), (39, 2))

    def test_Nr05_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([2, 3], [4, 0]), (8, 12))

    def test_Nr06_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([1, 1], [1, -1]), (2, 0))

    def test_Nr07_mnozenie_argumenty_tablica_tablica(self):
        self.assertEqual(mnozenie([0, 0], [1, 1]), (0, 0))

    def test_Nr01_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([1, 1], [1, -1]), (0.0, 1.0))

    def test_Nr02_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([0, 0], [1, 1]), (0.0, 0.0))

    def test_Nr03_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([-1, -1], [1, -1]), (0.0, -1.0))

    def test_Nr04_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([3, 4], [1, 1]), (3.5, 0.5))

    def test_Nr05_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([5, 2], [2, 1]), (2.4, -0.2))

    def test_Nr07_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([0, 5], [1, 1]), (2.5, 2.5))

    def test_Nr08_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([7, 0], [3, 4]), (0.84, -1.12))

    def test_Nr09_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([-4, 2], [-1, -1]), (1.0, -3.0))

    def test_Nr10_dzielenie_argumenty_tablica_tablica(self):
        self.assertEqual(dzielenie([12, 16], [4, 0]), (3.0, 4.0))

    def test_Nr01_potegowanie_argumenty_tablica_2(self):
        self.assertEqual(potegowanie([1, 1], 2), (0, 2))

    def test_Nr02_potegowanie_argumenty_tablica_3(self):
        self.assertEqual(potegowanie([1, 1], 3), (-2, 2))

    def test_Nr03_potegowanie_argumenty_tablica_3(self):
        self.assertEqual(potegowanie([2, 0], 3), (8, 0))

    def test_Nr04_potegowanie_argumenty_tablica_4(self):
        self.assertEqual(potegowanie([0, 1], 4), (1, 0))

    def test_Nr05_potegowanie_argumenty_tablica_2(self):
        self.assertEqual(potegowanie([1, -1], 2), (0, -2))

    def test_Nr06_potegowanie_argumenty_tablica_2(self):
        self.assertEqual(potegowanie([-1, -1], 2), (0, 2))

    def test_Nr07_potegowanie_argumenty_tablica_3(self):
        self.assertEqual(potegowanie([3, 4], 3), (-117, 44))

    def test_Nr08_potegowanie_argumenty_tablica_3(self):
        self.assertEqual(potegowanie([-2, 0], 3), (-8, 0))

    def test_Nr09_potegowanie_argumenty_tablica_8(self):
        self.assertEqual(potegowanie([1, -1], 8), (16, 0))

    def test_Nr10_potegowanie_argumenty_tablica_6(self):
        self.assertEqual(potegowanie([2, 2], 6), (0, -512))
