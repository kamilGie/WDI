import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon135 import Zadanie_135


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

    def test_Nr01_Zadanie_135_argumenty_tablica_0(self):
            self.assertEqual(Zadanie_135([[1, 2, 3, 4, 5, 6, 7, 8], [2, 1, 2, 3, 4, 5, 6, 7], [3, 2, 1, 2, 3, 4, 5, 6], [4, 3, 2, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 2, 3, 4], [6, 5, 4, 3, 2, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1, 2], [8, 7, 6, 5, 4, 3, 2, 1]], 0), 8)

    def test_Nr02_Zadanie_135_argumenty_tablica_3(self):
            self.assertEqual(Zadanie_135([[5, 4, 3, 2, 1, 2, 3, 4], [6, 5, 4, 3, 2, 3, 4, 5], [7, 6, 5, 4, 3, 4, 5, 6], [8, 7, 6, 5, 4, 5, 6, 7], [9, 8, 7, 6, 5, 6, 7, 8], [10, 9, 8, 7, 6, 7, 8, 9], [11, 10, 9, 8, 7, 8, 9, 10], [12, 11, 10, 9, 8, 9, 10, 11]], 3), 37)

    def test_Nr03_Zadanie_135_argumenty_tablica_5(self):
            self.assertEqual(Zadanie_135([[1, 3, 2, 4, 1, 3, 2, 4], [2, 4, 3, 5, 2, 4, 3, 5], [3, 5, 4, 6, 3, 5, 4, 6], [4, 6, 5, 7, 4, 6, 5, 7], [5, 7, 6, 8, 5, 7, 6, 8], [6, 8, 7, 9, 6, 8, 7, 9], [7, 9, 8, 10, 7, 9, 8, 10], [8, 10, 9, 11, 8, 10, 9, 11]], 5), 38)

    def test_Nr04_Zadanie_135_argumenty_tablica_3(self):
            self.assertEqual(Zadanie_135([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], 3), 8)

    def test_Nr05_Zadanie_135_argumenty_tablica_2(self):
            self.assertEqual(Zadanie_135([[2, 3, 1, 4, 6, 5, 7, 8], [5, 4, 6, 1, 3, 2, 4, 5], [6, 7, 3, 2, 4, 5, 3, 6], [1, 2, 5, 4, 7, 3, 1, 2], [3, 5, 6, 7, 4, 2, 5, 1], [2, 4, 5, 6, 7, 1, 2, 3], [3, 5, 1, 2, 6, 7, 5, 4], [7, 8, 2, 3, 1, 4, 6, 5]], 2), 17)

    def test_Nr06_Zadanie_135_argumenty_tablica_4(self):
            self.assertEqual(Zadanie_135([[4, 2, 1, 3, 5, 6, 4, 7], [3, 5, 2, 4, 1, 3, 6, 5], [6, 3, 7, 1, 4, 2, 5, 4], [5, 6, 2, 4, 3, 1, 6, 2], [7, 4, 3, 6, 5, 2, 3, 1], [4, 1, 5, 2, 3, 4, 2, 3], [5, 2, 4, 6, 1, 3, 7, 5], [3, 4, 5, 1, 2, 6, 3, 4]], 4), 16)

    def test_Nr07_Zadanie_135_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_135([[8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [2, 1, 4, 3, 6, 5, 8, 7], [3, 2, 5, 4, 7, 6, 1, 8], [4, 3, 6, 5, 8, 7, 2, 1], [5, 4, 7, 6, 1, 8, 3, 2], [6, 5, 8, 7, 2, 1, 4, 3], [7, 6, 1, 8, 3, 2, 5, 4]], 6), 21)

    def test_Nr08_Zadanie_135_argumenty_tablica_0(self):
            self.assertEqual(Zadanie_135([[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [5, 6, 7, 8, 1, 2, 3, 4], [4, 3, 2, 1, 8, 7, 6, 5], [7, 8, 1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1, 8, 7], [3, 4, 5, 6, 7, 8, 1, 2], [2, 1, 8, 7, 6, 5, 4, 3]], 0), 24)

    def test_Nr09_Zadanie_135_argumenty_tablica_7(self):
            self.assertEqual(Zadanie_135([[9, 8, 7, 6, 5, 4, 3, 2], [2, 3, 4, 5, 6, 7, 8, 9], [1, 9, 8, 7, 6, 5, 4, 3], [3, 2, 1, 9, 8, 7, 6, 5], [7, 6, 5, 4, 3, 2, 1, 9], [8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2], [2, 3, 4, 5, 6, 7, 8, 9]], 7), 30)

    def test_Nr10_Zadanie_135_argumenty_tablica_1(self):
            self.assertEqual(Zadanie_135([[3, 5, 1, 2, 4, 6, 7, 8], [7, 3, 5, 1, 6, 4, 2, 5], [4, 7, 2, 6, 3, 5, 1, 4], [6, 2, 3, 7, 5, 1, 4, 6], [5, 4, 6, 1, 2, 7, 3, 2], [2, 5, 4, 6, 7, 1, 3, 5], [1, 6, 2, 4, 5, 3, 7, 6], [8, 7, 5, 3, 1, 6, 4, 2]], 1), 23)


