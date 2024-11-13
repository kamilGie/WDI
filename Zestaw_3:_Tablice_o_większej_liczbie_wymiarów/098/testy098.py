import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon098 import Zadanie_98


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

    def test_Nr01_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[1, 3, 5], [2, 4, 6], [7, 8, 9]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_Nr02_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[10, 15], [5, 20]], [0, 0, 0, 0]), [5, 10, 15, 20])

    def test_Nr03_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[0, 0, 0], [1, 2, 3], [4, 5, 6]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 1, 2, 3, 4, 5, 6])

    def test_Nr04_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[4], [2], [7]], [0, 0, 0]), [2, 4, 7])

    def test_Nr05_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[1]], [0]), [1])

    def test_Nr06_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([], []), [])

    def test_Nr07_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_Nr08_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[100, 200, 300], [150, 250, 350], [400, 500, 600]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [100, 150, 200, 250, 300, 350, 400, 500, 600])

    def test_Nr09_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[3, 6, 9], [12, 15, 18], [21, 24, 27]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_Nr10_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[10, 20], [30, 40]], [0, 0, 0, 0]), [10, 20, 30, 40])

    def test_Nr11_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[9, 9, 9], [9, 9, 9], [9, 9, 9]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [9, 9, 9, 9, 9, 9, 9, 9, 9])

    def test_Nr12_Zadanie_98_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_98([[0, 2, 4], [6, 8, 10], [12, 14, 16]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 2, 4, 6, 8, 10, 12, 14, 16])


