import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon67 import Zadanie_67


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

    def test_Nr01_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([6, 2, 3, 5, 1, 2]), True)
    def test_Nr02_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([4, 6, 8, 10, 12]), True)
    def test_Nr03_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([2, 3, 5, 7, 11]), False)
    def test_Nr04_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([1]), True)
    def test_Nr05_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([1, 4, 6]), False)
    def test_Nr06_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([10, 15, 21, 33, 39]), False)
    def test_Nr07_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([2, 3, 5, 7, 11]), False)
    def test_Nr08_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([10, 15, 1, 7, 1, 14, 2]), False)
    def test_Nr09_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([4, 8, 12, 16, 20]), True)
    def test_Nr10_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([0, 2, 4, 0, 6]), False)
    def test_Nr11_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([21, 34, 55, 89, 144]), False)
    def test_Nr12_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([7, 11, 13, 17, 19]), False)
    def test_Nr13_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([1, 2, 3, 4, 5]), False)
    def test_Nr14_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([10, 1, 4, 2, 3]), True)
    def test_Nr15_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([12, 15, 20, 25, 30, 6, 9]), True)
    def test_Nr16_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([17, 21, 29, 33, 37, 2]), False)
    def test_Nr17_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([0, 1, 2]), False)
    def test_Nr18_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([1, 2, 4, 3, 5, 6]), False)
    def test_Nr19_Zadanie_67_argumenty_tablica(self):
        self.assertEqual(Zadanie_67([2115, 1]), False)

