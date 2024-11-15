import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon100 import Zadanie_100


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

    def test_Nr01_Zadanie_100_argumenty_tablica_45(self):
            self.assertEqual(Zadanie_100([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45), False)

    def test_Nr02_Zadanie_100_argumenty_tablica_189(self):
            self.assertEqual(Zadanie_100([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 189), (1, 1))

    def test_Nr03_Zadanie_100_argumenty_tablica_1(self):
            self.assertEqual(Zadanie_100([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1), (1, 1))

    def test_Nr04_Zadanie_100_argumenty_tablica_2401(self):
            self.assertEqual(Zadanie_100([[1, 2, 3, 4, 5], [6, 7, 7, 7, 8], [9, 7, 5, 7, 10], [11, 7, 7, 7, 12], [13, 14, 15, 16, 17]], 2401), (2, 2))

    def test_Nr05_Zadanie_100_argumenty_tablica_1874161(self):
            self.assertEqual(Zadanie_100([[13, 2, 3, 4, 17], [6, 7, 7, 7, 8], [9, 7, 5, 7, 10], [11, 7, 7, 7, 12], [13, 14, 15, 16, 17]], 1874161), False)

    def test_Nr06_Zadanie_100_argumenty_tablica_2401(self):
            self.assertEqual(Zadanie_100([[13, 2, 3, 4, 17], [6, 7, 7, 7, 8], [9, 7, 5, 7, 10], [11, 7, 7, 7, 12], [13, 14, 15, 16, 17]], 2401), (2, 2))

    def test_Nr07_Zadanie_100_argumenty_tablica_48841(self):
            self.assertEqual(Zadanie_100([[13, 2, 3, 4, 17], [6, 7, 7, 7, 8], [9, 7, 5, 7, 10], [11, 7, 7, 7, 12], [13, 14, 15, 16, 17]], 48841), (2, 2))

    def test_Nr08_Zadanie_100_argumenty_tablica_28561(self):
            self.assertEqual(Zadanie_100([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 13, 13, 13, 13, 17], [18, 19, 13, 20, 21, 13, 22], [23, 24, 13, 25, 26, 13, 27], [28, 29, 13, 13, 13, 13, 30], [31, 32, 33, 34, 35, 36, 37]], 28561), False)

    def test_Nr09_Zadanie_100_argumenty_tablica_0(self):
            self.assertEqual(Zadanie_100([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 13, 13, 13, 13, 17], [18, 19, 13, 20, 21, 13, 22], [23, 24, 13, 25, 26, 13, 27], [28, 29, 13, 13, 13, 13, 30], [31, 32, 33, 34, 35, 36, 37]], 0), False)

    def test_Nr10_Zadanie_100_argumenty_tablica_909090(self):
            self.assertEqual(Zadanie_100([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 13, 13, 13, 13, 17], [18, 19, 13, 20, 21, 13, 22], [23, 24, 13, 25, 26, 13, 27], [28, 29, 13, 13, 13, 13, 30], [31, 32, 33, 34, 35, 36, 37]], 909090), (5, 5))

    def test_Nr11_Zadanie_100_argumenty_tablica_239616(self):
            self.assertEqual(Zadanie_100([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 13, 13, 13, 13, 17], [18, 19, 13, 20, 21, 13, 22], [23, 24, 13, 25, 26, 13, 27], [28, 29, 13, 13, 13, 13, 30], [31, 32, 33, 34, 35, 36, 37]], 239616), (4, 3))


