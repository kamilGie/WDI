import unittest
import os
import sys
import importlib

from szablon138 import Zadanie_138


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

    def test_Nr01_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([1, 7, 3, 5, 11, 2]), 10)

    def test_Nr02_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([10, 15, 5, 3]), 3)

    def test_Nr03_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([2, 2, 2, 2, 2]), 2)

    def test_Nr07_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([8, 1, 2, 5]), 2)

    def test_Nr10_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([1, 1, 1, 1, 1]), 1)

    def test_Nr13_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([1, 1, 3, 4, 7]), 1)

    def test_Nr15_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([6, 8, 2, 3]), 3)

    def test_Nr19_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([1, 2, 2, 4, 7, 10]), 2)

    def test_Nr24_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([3, 7, 1, 4, 10]), 5)

    def test_Nr28_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([2, 1, 1, 3, 5]), 3)

    def test_Nr29_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([1, 1, 1, 1, 1, 1]), 1)

    def test_Nr35_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([10, 5, 2, 4, 8]), 2)

    def test_Nr36_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([2, 1, 4, 7, 5]), 1)

    def test_Nr39_Zadanie_138_argumenty_tablica(self):
        self.assertEqual(Zadanie_138([2, 1, 4, 7, 5]), 1)
