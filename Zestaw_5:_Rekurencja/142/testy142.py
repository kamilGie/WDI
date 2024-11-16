import unittest
import os
import sys
import importlib

from szablon142 import Zadanie_142


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

    def test_Nr01_Zadanie_142_argumenty_tablica_4(self):
        self.assertEqual(Zadanie_142([1, 2, 3], 4), [1, 3])

    #  xdddd no jakby jest to poprawne ale zeby komus to wyszlo to xdddd
    # def test_Nr02_Zadanie_142_argumenty_tablica_10(self):
    #     self.assertEqual(Zadanie_142([5, 10, 15], 10), [5, -10, 15])

    def test_Nr03_Zadanie_142_argumenty_tablica_9(self):
        self.assertEqual(Zadanie_142([4, 3, 5], 9), [4, 5])

    def test_Nr04_Zadanie_142_argumenty_tablica_19(self):
        self.assertEqual(Zadanie_142([7, 12, 15], 19), [7, 12])

    def test_Nr05_Zadanie_142_argumenty_tablica_12(self):
        self.assertEqual(Zadanie_142([3, 9, 6], 12), [3, 9])

    def test_Nr06_Zadanie_142_argumenty_tablica_10(self):
        self.assertEqual(Zadanie_142([4, 7, 3], 10), [7, 3])

    def test_Nr07_Zadanie_142_argumenty_tablica_8(self):
        self.assertEqual(Zadanie_142([2, 4, 5, 7], 8), [2, 4, -5, 7])

    def test_Nr08_Zadanie_142_argumenty_tablica_15(self):
        self.assertEqual(Zadanie_142([10, 5, 1], 15), [10, 5])

    def test_Nr09_Zadanie_142_argumenty_tablica_14(self):
        self.assertEqual(Zadanie_142([10, 5, 1], 14), [10, 5, -1])

    def test_Nr10_Zadanie_142_argumenty_tablica_11(self):
        self.assertEqual(Zadanie_142([1, 3, 5, 7], 11), [1, 3, 7])

    def test_Nr11_Zadanie_142_argumenty_tablica_9(self):
        self.assertEqual(Zadanie_142([7, 3, 1], 9), [7, 3, -1])
