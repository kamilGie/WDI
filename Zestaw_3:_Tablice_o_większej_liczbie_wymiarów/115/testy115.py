import unittest
import os
import sys
import importlib

from szablon115 import four


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

    def test_Nr01_four_argumenty_tablica(self):
        self.assertEqual(four([[2, 21, 5], [21, 24, 21], [17, 21, 23]]), 1)

    def test_Nr02_four_argumenty_tablica(self):
        self.assertEqual(four([[2, 6, 5], [6, 6, 6], [2, 2, 23]]), 0)

    def test_Nr03_four_argumenty_tablica(self):
        self.assertEqual(four([[2, 2, 5], [2, 6, 3], [2, 2, 23]]), 1)

    def test_Nr04_four_argumenty_tablica(self):
        self.assertEqual(four([[2, 2, 5], [2, 6, 3], [2, 5, 23]]), 0)

    def test_Nr05_four_argumenty_tablica(self):
        self.assertEqual(four([[2, 2, 5], [2, 6, 3], [2, 12, 23]]), 0)

    def test_Nr15_four_argumenty_tablica(self):
        self.assertEqual(
            four([[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]), 4
        )

    def test_Nr06_four_argumenty_tablica(self):
        self.assertEqual(
            four([[24, 21, 15, 10], [12, 14, 18, 20], [32, 34, 27, 30], [8, 6, 9, 5]]),
            1,
        )

    def test_Nr07_four_argumenty_tablica(self):
        self.assertEqual(
            four([[6, 10, 15, 9], [14, 21, 18, 12], [20, 35, 22, 25], [8, 16, 27, 11]]),
            0,
        )

    def test_Nr09_four_argumenty_tablica(self):
        self.assertEqual(four([[2, 3, 5], [7, 11, 13], [17, 19, 23]]), 0)

    def test_Nr10_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [
                    [30, 45, 60, 75],
                    [12, 18, 24, 36],
                    [20, 25, 50, 100],
                    [15, 30, 45, 60],
                ]
            ),
            0,
        )

    def test_Nr11_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [[8, 16, 24, 32], [10, 20, 30, 40], [12, 22, 32, 42], [14, 24, 34, 44]]
            ),
            2,
        )

    def test_Nr12_four_argumenty_tablica(self):
        self.assertEqual(four([[6, 9], [12, 15]]), 0)

    def test_Nr13_four_argumenty_tablica(self):
        self.assertEqual(
            four([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]), 0
        )

    def test_Nr14_four_argumenty_tablica(self):
        self.assertEqual(
            four([[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]), 4
        )

    def test_Nr16_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [[24, 36, 48, 60], [28, 42, 56, 70], [12, 18, 24, 30], [8, 16, 32, 40]]
            ),
            0,
        )

    def test_Nr17_four_argumenty_tablica(self):
        self.assertEqual(four([[5, 10, 15], [7, 14, 21], [8, 16, 24]]), 1)

    def test_Nr19_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [[9, 18, 27, 36], [12, 24, 36, 48], [15, 30, 45, 60], [21, 42, 63, 84]]
            ),
            0,
        )

    def test_Nr20_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [[8, 16, 24, 32], [10, 20, 30, 40], [12, 22, 32, 42], [14, 24, 34, 44]]
            ),
            2,
        )

    def test_Nr21_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [
                    [30, 45, 60, 75, 90, 105, 120],
                    [12, 18, 24, 36, 48, 60, 72],
                    [20, 30, 40, 50, 60, 70, 80],
                    [14, 21, 28, 35, 42, 49, 56],
                    [25, 50, 75, 100, 125, 150, 175],
                    [12, 18, 24, 30, 36, 42, 48],
                    [6, 12, 18, 24, 30, 36, 42],
                ]
            ),
            1,
        )

    def test_Nr22_four_argumenty_tablica(self):
        self.assertEqual(
            four(
                [
                    [120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200],
                    [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
                    [80, 160, 240, 320, 400, 480, 560, 640, 720, 800],
                    [60, 120, 180, 240, 300, 360, 420, 480, 540, 600],
                    [40, 80, 120, 160, 200, 240, 280, 320, 360, 400],
                    [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],
                    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                    [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
                    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                ]
            ),
            0,
        )
