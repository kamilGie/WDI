import unittest
from contextlib import redirect_stdout
import io

from szablon2022_B2 import square


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
    import os
    import sys
    import importlib
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_square(self):
            self.assertEqual(square([    [2, 3, 5],    [1, 1, 13],    [2, 6, 23]]), 2)

    def test_Nr02_square(self):
            self.assertEqual(square([    [2, 3, 5],    [1, 1, 13],    [2, 3, 23]]), 2)

    def test_Nr03_square(self):
            self.assertEqual(square([    [2, 3, 5],    [1, 1, 13],    [1, 6, 23]]), 2)

    def test_Nr04_square(self):
            self.assertEqual(square([    [1, 3, 1],    [17, 5, 13],    [5, 6, 6]]), 0)

    def test_Nr05_square(self):
            self.assertEqual(square([    [1, 3, 1],    [17, 5, 13],    [1, 6, 6]]), 0)

    def test_Nr06_square(self):
            self.assertEqual(square([    [1, 3, 1],    [17, 1, 1],    [1, 1, 6]]), 2)

    def test_Nr07_square(self):
            self.assertEqual(square([    [2, 3, 5, 7],    [6, 10, 15, 21],    [14, 22, 33, 35],    [26, 34, 55, 77]]), 0)

    def test_Nr08_square(self):
            self.assertEqual(square([    [2, 3, 5, 7],    [6, 6, 15, 21],    [14, 22, 33, 35],    [26, 34, 55, 77]]), 2)

    def test_Nr09_square(self):
            self.assertEqual(square([    [2, 5, 6, 7],    [6, 6, 15, 21],    [3, 22, 3, 35],    [26, 34, 55, 77]]), 3)

    def test_Nr10_square(self):
            self.assertEqual(square([    [6, 10, 15, 21, 33],    [14, 22, 26, 34, 55],    [10, 15, 21, 35, 77],    [14, 21, 33, 77, 91],    [22, 26, 34, 55, 77]]), 0)

    def test_Nr11_square(self):
            self.assertEqual(square([    [6, 10, 15, 21, 33],    [14, 6, 26, 34, 6],    [10, 15, 21, 35, 77],    [14, 21, 33, 77, 91],    [22, 6, 34, 55, 6]]), 4)

    def test_Nr12_square(self):
            self.assertEqual(square([    [6, 10, 15, 21, 33],    [14, 6, 6, 6, 6],    [10, 15, 6, 6, 77],    [14, 21, 33, 77, 91],    [22, 6, 34, 55, 6]]), 2)

    def test_Nr13_square(self):
            self.assertEqual(square([    [6, 10, 15, 21, 33],    [14, 6, 6, 6, 6],    [10, 15, 5, 6, 77],    [14, 21, 33, 77, 91],    [22, 6, 34, 55, 6]]), 4)


