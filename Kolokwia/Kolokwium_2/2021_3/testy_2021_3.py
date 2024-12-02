import unittest
import os
import sys
import importlib

from szablon_2021_3 import Zadanie_3


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

    def test_Nr01_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[2, 3, 5], [3, 1, 7], [5, 7, 11]]), 0)

    def test_Nr02_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[2, 3, 3], [3, 1, 3], [5, 7, 11]]), 1)

    def test_Nr03_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[3, 3, 3], [3, 1, 10], [5, 7, 11]]), 2)

    def test_Nr04_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[3, 2, 3], [3, 1, 3], [3, 2, 3]]), 0)

    def test_Nr05_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[3, 2, 2], [3, 1, 3], [3, 2, 3]]), 1)

    def test_Nr06_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[3, 2, 2], [2, 1, 3], [3, 2, 3]]), 1)

    def test_Nr07_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(Zadanie_3([[3, 2, 2], [2, 1, 3], [3, 2, 2]]), 0)

    def test_Nr09_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [1, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                    [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
                    [5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
                    [7, 11, 13, 17, 19, 23, 29, 31, 37, 41],
                    [11, 13, 17, 19, 23, 29, 31, 37, 41, 43],
                    [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
                    [17, 19, 23, 29, 31, 37, 41, 43, 47, 53],
                    [19, 23, 29, 31, 37, 41, 43, 47, 53, 59],
                    [23, 29, 31, 37, 41, 43, 47, 53, 59, 61],
                    [29, 31, 37, 41, 43, 47, 53, 59, 61, 67],
                ]
            ),
            0,
        )

    def test_Nr10_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [1, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                    [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
                    [5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
                    [10, 11, 13, 17, 19, 23, 29, 31, 37, 41],
                    [11, 13, 17, 19, 23, 29, 31, 37, 41, 43],
                    [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
                    [17, 19, 23, 29, 31, 37, 41, 43, 47, 53],
                    [19, 23, 29, 31, 37, 41, 43, 47, 53, 59],
                    [23, 29, 31, 37, 41, 43, 47, 53, 59, 61],
                    [29, 31, 37, 41, 43, 47, 53, 59, 61, 67],
                ]
            ),
            2,
        )

    def test_Nr11_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [1, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                    [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
                    [5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
                    [10, 11, 13, 17, 19, 23, 29, 31, 37, 62],
                    [11, 13, 17, 19, 23, 29, 31, 37, 41, 43],
                    [13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
                    [17, 19, 23, 29, 31, 37, 41, 43, 47, 53],
                    [19, 23, 29, 31, 37, 41, 43, 47, 53, 59],
                    [23, 29, 31, 37, 41, 43, 47, 53, 59, 61],
                    [29, 31, 37, 41, 43, 47, 53, 59, 61, 67],
                ]
            ),
            2,
        )

    def test_Nr12_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                ]
            ),
            0,
        )

    def test_Nr13_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [1, 2, 3, 4, 5, 7, 8, 9, 10, 11],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                ]
            ),
            0,
        )

    def test_Nr14_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [2, 2, 3, 4, 5, 7, 8, 9, 10, 11],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                ]
            ),
            2,
        )

    def test_Nr15_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [2, 2, 3, 4, 5, 7, 8, 9, 10, 10],
                    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                ]
            ),
            2,
        )

    def test_Nr16_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ]
            ),
            0,
        )

    def test_Nr17_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ]
            ),
            0,
        )

    def test_Nr18_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 2],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ]
            ),
            2,
        )

    def test_Nr19_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
                    [2, 3, 2, 3, 2, 2, 2, 3, 2, 3],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ]
            ),
            0,
        )

    def test_Nr20_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
                    [2, 3, 2, 3, 2, 2, 2, 3, 2, 3],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [4, 4, 4, 4, 4, 1, 4, 4, 4, 4],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                ]
            ),
            0,
        )

    def test_Nr21_Zadanie_116_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_3(
                [
                    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],
                    [2, 3, 2, 3, 2, 2, 2, 3, 2, 3],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [4, 4, 4, 4, 4, 1, 4, 4, 3, 4],
                    [1, 1, 1, 1, 1, 1, 2, 3, 3, 1],
                ]
            ),
            2,
        )
