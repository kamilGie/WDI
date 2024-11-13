import unittest
import os
import sys
import importlib

from szablon111 import Zadanie_111


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

    def test_Nr01_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), ([1, 1], [2, 2])
        )

    def test_Nr02_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
            ),
            ([2, 2], [3, 3]),
        )

    def test_Nr03_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), ([0, 0], [1, 1])
        )

    def test_Nr04_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(Zadanie_111([[10, 20], [30, 40]]), ([0, 0], [1, 1]))

    def test_Nr05_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(Zadanie_111([[-10, -20], [-30, -40]]), ([0, 0], [1, 1]))

    def test_Nr06_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), ([0, 0], [1, 1])
        )

    def test_Nr07_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111([[100, 200, 300], [400, 500, 600], [700, 800, 900]]),
            ([1, 1], [2, 2]),
        )

    def test_Nr08_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]), ([1, 0], [2, 2])
        )

    def test_Nr09_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111(
                [
                    [37, -48, 39, -16, 1, 44, 30, -5],
                    [-45, 7, 18, -33, -35, -45, -14, -50],
                    [-27, -9, 44, -23, 40, -38, -22, -19],
                    [1, 34, 12, -41, -47, -40, -17, 25],
                    [-47, -4, -38, 8, 47, 30, -14, 3],
                    [45, -14, -9, -48, 8, 27, 43, -29],
                    [-15, 14, 6, -9, -14, 46, 18, -13],
                    [43, -30, -33, -50, 44, -29, 50, -5],
                ]
            ),
            ([0, 4], [6, 6]),
        )

    def test_Nr10_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111(
                [
                    [10, -23, 3, -5, 14, 7, -12, 11],
                    [-6, 21, -4, 16, 20, -18, -13, 25],
                    [-9, 8, -10, 22, -5, 19, 6, -2],
                    [12, 3, 17, -14, -3, 18, 20, -7],
                    [7, -1, 5, -6, 9, -11, -16, 13],
                    [11, 6, -20, 8, 3, 14, -2, 17],
                    [-3, -16, 18, 25, -9, 12, -8, 15],
                    [9, 13, -4, 5, 2, -6, 20, -11],
                ]
            ),
            ([3, 3], [7, 7]),
        )

    def test_Nr11_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111(
                [
                    [1, -2, 3, -4, 5, -6, 7, -8],
                    [-9, 10, -11, 12, -13, 14, -15, 16],
                    [17, -18, 19, -20, 21, -22, 23, -24],
                    [25, -26, 27, -28, 29, -30, 31, -32],
                    [33, -34, 35, -36, 37, -38, 39, -40],
                    [41, -42, 43, -44, 45, -46, 47, -48],
                    [49, -50, 51, -52, 53, -54, 55, -56],
                    [57, -58, 59, -60, 61, -62, 63, -64],
                ]
            ),
            ([0, 4], [1, 6]),
        )

    def test_Nr12_Zadanie_111_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_111(
                [
                    [21, -75, 12, -34, 58, -12, 4, -56],
                    [-98, 37, -63, 22, -41, 15, 18, -71],
                    [66, 99, -8, -40, 27, 19, 56, -85],
                    [32, -13, 67, 23, 74, -58, 6, -4],
                    [-50, 41, 15, 88, -10, -36, 61, -29],
                    [-72, -80, 53, 22, 90, -21, -58, 25],
                    [38, 15, -67, 42, 6, 76, -99, 47],
                    [-39, 18, -2, 30, 9, -50, 72, 28],
                ]
            ),
            ([2, 3], [4, 4]),
        )
