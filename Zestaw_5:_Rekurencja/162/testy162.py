import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon162 import Zadanie_162


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

    def test_Nr01_Zadanie_162_argumenty_tablica_1(self):
            self.assertEqual(Zadanie_162([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]], 1), True)

    def test_Nr02_Zadanie_162_argumenty_tablica_1_0f(self):
            self.assertEqual(Zadanie_162([[2, 0, 0], [0, 2, 0], [0, 0, 2], [1, 1, 1]], 1.0), False)

    def test_Nr03_Zadanie_162_argumenty_tablica_1_0f(self):
            self.assertEqual(Zadanie_162([[0, 0, 0], [1, 1, 1]], 1.0), False)

    def test_Nr04_Zadanie_162_argumenty_tablica_1_5f(self):
            self.assertEqual(Zadanie_162([[0.5, 0.5, 0.5], [1.0, 1.0, 1.0], [1.5, 1.5, 1.5], [2.0, 2.0, 2.0]], 1.5), False)

    def test_Nr05_Zadanie_162_argumenty_tablica_2_0f(self):
            self.assertEqual(Zadanie_162([[3, 0, 0], [0, 4, 0], [0, 0, 5], [0, 0, 0]], 2.0), True)

    def test_Nr06_Zadanie_162_argumenty_tablica_1_0f(self):
            self.assertEqual(Zadanie_162([[1, 1, 0], [0, 1, 1], [1, 0, 1]], 1.0), False)

    def test_Nr07_Zadanie_162_argumenty_tablica_1_0f(self):
            self.assertEqual(Zadanie_162([[0, 0, 0], [0.5, 0.5, 0.5], [1, 1, 1]], 1.0), True)

    def test_Nr08_Zadanie_162_argumenty_tablica_1_0f(self):
            self.assertEqual(Zadanie_162([[0, 0, 0], [0.5, 0.5, 0.5], [1, 1, 1]], 1.0), True)

    def test_Nr09_Zadanie_162_argumenty_tablica_6_0f(self):
            self.assertEqual(Zadanie_162([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 6.0), False)

    def test_Nr10_Zadanie_162_argumenty_tablica_5_0f(self):
            self.assertEqual(Zadanie_162([[0, 0, 0], [2, 2, 2], [4, 4, 4], [6, 6, 6]], 5.0), True)

    def test_Nr11_Zadanie_162_argumenty_tablica_1_0f(self):
            self.assertEqual(Zadanie_162([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [0.5, 0.5, 0.5]], 1.0), True)

    def test_Nr12_Zadanie_162_argumenty_tablica_2_0f(self):
            self.assertEqual(Zadanie_162([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 2.0), True)

    def test_Nr13_Zadanie_162_argumenty_tablica_3_0f(self):
            self.assertEqual(Zadanie_162([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]], 3.0), False)

    def test_Nr14_Zadanie_162_argumenty_tablica_2_0f(self):
            self.assertEqual(Zadanie_162([[0.5, 0.5, 0.5], [1.5, 1.5, 1.5], [2.5, 2.5, 2.5]], 2.0), False)

    def test_Nr15_Zadanie_162_argumenty_tablica_5_0f(self):
            self.assertEqual(Zadanie_162([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5.0), False)

    def test_Nr16_Zadanie_162_argumenty_tablica_5_0f(self):
            self.assertEqual(Zadanie_162([[0, 0, 0], [3, 3, 3], [6, 6, 6], [9, 9, 9]], 5.0), False)

    def test_Nr17_Zadanie_162_argumenty_tablica_2_0f(self):
            self.assertEqual(Zadanie_162([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2.0), False)

    def test_Nr18_Zadanie_162_argumenty_tablica_3_0f(self):
            self.assertEqual(Zadanie_162([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3.0), False)

    def test_Nr19_Zadanie_162_argumenty_tablica_3_0f(self):
            self.assertEqual(Zadanie_162([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]], 3.0), False)


