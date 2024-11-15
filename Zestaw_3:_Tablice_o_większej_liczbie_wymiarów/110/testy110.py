import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon110 import Zadanie_110


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

    def test_Nr01_Zadanie_110_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_110([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6), 1)

    def test_Nr02_Zadanie_110_argumenty_tablica_4(self):
            self.assertEqual(Zadanie_110([[1, 2], [3, 4]], 4), 0)

    def test_Nr03_Zadanie_110_argumenty_tablica_18(self):
            self.assertEqual(Zadanie_110([[2, 3], [6, 9]], 18), 0)

    def test_Nr04_Zadanie_110_argumenty_tablica_12(self):
            self.assertEqual(Zadanie_110([[2, 4, 1], [3, 1, 2], [6, 5, 4]], 12), 2)

    def test_Nr05_Zadanie_110_argumenty_tablica_12(self):
            self.assertEqual(Zadanie_110([[5, 2, 3], [1, 6, 8], [9, 7, 4]], 12), 0)

    def test_Nr06_Zadanie_110_argumenty_tablica_18(self):
            self.assertEqual(Zadanie_110([[1, 2, 4], [5, 6, 3], [8, 7, 9]], 18), 1)

    def test_Nr07_Zadanie_110_argumenty_tablica_12(self):
            self.assertEqual(Zadanie_110([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 12), 1)

    def test_Nr08_Zadanie_110_argumenty_tablica_1(self):
            self.assertEqual(Zadanie_110([[1]], 1), 0)

    def test_Nr09_Zadanie_110_argumenty_tablica_30(self):
            self.assertEqual(Zadanie_110([[5, 3], [1, 6]], 30), 0)

    def test_Nr10_Zadanie_110_argumenty_tablica_12(self):
            self.assertEqual(Zadanie_110([[2, 4, 3], [1, 7, 2], [6, 5, 9]], 12), 1)


