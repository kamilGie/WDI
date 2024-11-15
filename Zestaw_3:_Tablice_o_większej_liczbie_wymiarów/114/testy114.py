import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon114 import chess


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

    def test_Nr01_chess_argumenty_tablica(self):
            self.assertEqual(chess([[4, 0, 2], [3, 0, 0], [6, 5, 3]]), (0, 1, 1, 0))

    def test_Nr02_chess_argumenty_tablica(self):
            self.assertEqual(chess([[1, 1, 2, 3], [-1, 3, -1, 4], [4, 1, 5, 4], [5, 0, 3, 6]]), (2, 3, 3, 1))

    def test_Nr03_chess_argumenty_tablica(self):
            self.assertEqual(chess([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (0, 0, 1, 1))

    def test_Nr04_chess_argumenty_tablica(self):
            self.assertEqual(chess([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), (0, 2, 2, 2))

    def test_Nr05_chess_argumenty_tablica(self):
            self.assertEqual(chess([[-1000, 1], [1, -1000]]), (0, 0, 1, 1))

    def test_Nr06_chess_argumenty_tablica(self):
            self.assertEqual(chess([[5, -1, 3, -4], [-2, 7, -6, 8], [9, 0, -3, 1], [4, -5, 2, -3]]), (1, 0, 1, 2))

    def test_Nr07_chess_argumenty_tablica(self):
            self.assertEqual(chess([[-1000, -1000], [2, 2]]), (0, 0, 0, 1))

    def test_Nr08_chess_argumenty_tablica(self):
            self.assertEqual(chess([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 100, 1], [1, 1, 1, 1]]), (0, 2, 1, 0))

    def test_Nr09_chess_argumenty_tablica(self):
            self.assertEqual(chess([[100, -50, -30, 20], [25, -15, -10, -5], [-20, 10, 30, -40], [5, 5, -100, 50]]), (2, 0, 2, 3))

    def test_Nr10_chess_argumenty_tablica(self):
            self.assertEqual(chess([[10, -5, 3, 1, 2, -7], [2, 0, -4, 6, 7, 9], [-1, 4, 8, -3, 5, 6], [7, 6, -8, 10, 12, -2], [3, -2, 9, 0, -6, 4], [-3, 4, 5, 2, -1, 8]]), (3, 2, 5, 0))

    def test_Nr11_chess_argumenty_tablica(self):
            self.assertEqual(chess([[2, 5, -3, 7, 1, 0, 4, -2], [4, 0, 1, -5, 6, 3, -1, 2], [-2, -7, 3, 2, 1, -8, 5, 6], [6, 5, -1, -2, 7, 4, 0, 3], [7, 8, 4, -3, 6, 2, 1, -5], [-1, 0, 3, 5, -4, 9, 7, 8], [4, -3, 0, 1, 7, 2, 6, 5], [8, 2, -6, 4, -5, 3, -2, 1]]), (5, 0, 6, 1))


