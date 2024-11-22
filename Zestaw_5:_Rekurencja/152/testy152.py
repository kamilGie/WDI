import unittest
import os
import sys
import importlib

from szablon152 import Zadanie_152


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

    def test_Nr01_Zadanie_152_argumenty_tablica_1_1(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 82, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 91, 2],
                    [1, 4, 6, 82, 3, 5, 24, 2],
                    [1, 4, 6, 2, 3, 5, 35, 7],
                    [1, 4, 6, 2, 3, 5, 35, 8],
                ],
                1,
                1,
            ),
            True,
        )

    def test_Nr02_Zadanie_152_argumenty_tablica_0_1(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 82, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 91, 2],
                    [1, 4, 6, 82, 3, 5, 24, 2],
                    [1, 4, 6, 2, 3, 5, 35, 7],
                    [1, 4, 6, 2, 3, 5, 35, 8],
                ],
                0,
                1,
            ),
            True,
        )

    def test_Nr03_Zadanie_152_argumenty_tablica_0_0(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [0, 1, 2, 3, 4, 5, 6, 7],
                    [1, 2, 3, 4, 5, 6, 7, 8],
                    [2, 3, 4, 5, 6, 7, 8, 9],
                    [3, 4, 5, 6, 7, 8, 9, 10],
                    [4, 5, 6, 7, 8, 9, 10, 11],
                    [5, 6, 7, 8, 9, 10, 11, 12],
                    [6, 7, 8, 9, 10, 11, 12, 13],
                    [7, 8, 9, 10, 11, 12, 13, 14],
                ],
                0,
                0,
            ),
            True,
        )

    def test_Nr05_Zadanie_152_argumenty_tablica_2_2(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8],
                    [2, 3, 4, 5, 6, 7, 8, 9],
                    [3, 4, 5, 6, 7, 8, 9, 10],
                    [4, 5, 6, 7, 8, 9, 10, 11],
                    [5, 6, 7, 8, 9, 10, 11, 12],
                    [6, 7, 8, 9, 10, 11, 12, 13],
                    [7, 8, 9, 10, 11, 12, 13, 14],
                    [8, 9, 10, 11, 12, 13, 14, 15],
                ],
                2,
                2,
            ),
            False,
        )

    def test_Nr06_Zadanie_152_argumenty_tablica_3_3(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [6, 7, 8, 9, 10, 11, 12, 13],
                    [7, 8, 9, 10, 11, 12, 13, 14],
                    [8, 9, 10, 11, 12, 13, 14, 15],
                    [9, 10, 11, 12, 13, 14, 15, 16],
                    [10, 11, 12, 13, 14, 15, 16, 17],
                    [11, 12, 13, 14, 15, 16, 17, 18],
                    [12, 13, 14, 15, 16, 17, 18, 19],
                    [13, 14, 15, 16, 17, 18, 19, 20],
                ],
                3,
                3,
            ),
            False,
        )

    def test_Nr08_Zadanie_152_argumenty_tablica_6_6(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8],
                    [0, 9, 10, 11, 12, 13, 14, 15],
                    [1, 9, 17, 25, 33, 41, 49, 57],
                    [3, 8, 16, 24, 32, 40, 48, 56],
                    [4, 7, 19, 26, 35, 43, 51, 59],
                    [2, 6, 18, 27, 36, 44, 52, 60],
                    [5, 8, 21, 29, 37, 45, 53, 61],
                    [1, 3, 20, 28, 38, 46, 54, 62],
                ],
                6,
                6,
            ),
            True,
        )

    def test_Nr09_Zadanie_152_argumenty_tablica_4_5(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [3, 2, 4, 1, 6, 5, 7, 8],
                    [1, 9, 10, 11, 12, 13, 14, 15],
                    [1, 9, 17, 25, 33, 41, 49, 57],
                    [3, 8, 16, 24, 32, 40, 48, 56],
                    [4, 7, 19, 26, 35, 43, 51, 59],
                    [2, 6, 18, 27, 36, 44, 52, 60],
                    [5, 8, 21, 29, 37, 45, 53, 61],
                    [1, 3, 20, 28, 38, 46, 54, 62],
                ],
                4,
                5,
            ),
            False,
        )

    def test_Nr10_Zadanie_152_argumenty_tablica_0_0(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [9, 2, 3, 4, 5, 6, 7, 8],
                    [1, 5, 10, 11, 12, 13, 14, 15],
                    [1, 3, 2, 4, 5, 6, 7, 8],
                    [1, 4, 3, 6, 5, 7, 8, 9],
                    [2, 8, 1, 5, 9, 10, 11, 12],
                    [1, 3, 6, 8, 9, 11, 5, 6],
                    [2, 1, 3, 7, 9, 12, 4, 6],
                    [4, 2, 1, 3, 5, 6, 7, 8],
                ],
                0,
                0,
            ),
            True,
        )

    def test_Nr11_Zadanie_152_argumenty_tablica_0_0(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [9, 2, 3, 4, 5, 6, 7, 8],
                    [1, 5, 10, 11, 12, 13, 14, 15],
                    [1, 3, 2, 4, 5, 6, 7, 8],
                    [1, 4, 3, 6, 5, 7, 8, 9],
                    [2, 8, 1, 5, 9, 10, 11, 12],
                    [1, 3, 6, 8, 9, 11, 5, 6],
                    [2, 1, 3, 7, 9, 12, 4, 6],
                    [4, 2, 1, 3, 5, 6, 7, 8],
                ],
                0,
                0,
            ),
            True,
        )

    def test_Nr12_Zadanie_152_argumenty_tablica_1_1(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8],
                    [0, 9, 10, 11, 12, 13, 14, 15],
                    [2, 9, 17, 25, 33, 41, 49, 57],
                    [4, 8, 16, 24, 32, 40, 48, 56],
                    [5, 7, 19, 26, 35, 43, 51, 59],
                    [3, 6, 18, 27, 36, 44, 52, 60],
                    [6, 8, 21, 29, 37, 45, 53, 61],
                    [2, 3, 20, 28, 38, 46, 54, 62],
                ],
                1,
                1,
            ),
            False,
        )

    def test_Nr13_Zadanie_152_argumenty_tablica_0_0(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [3, 4, 5, 6, 7, 8, 9, 10],
                    [0, 1, 2, 3, 4, 5, 6, 7],
                    [2, 3, 4, 5, 6, 7, 8, 9],
                    [3, 5, 7, 8, 9, 10, 11, 12],
                    [2, 5, 8, 9, 11, 12, 14, 15],
                    [4, 6, 8, 10, 11, 12, 13, 14],
                    [3, 5, 7, 9, 10, 12, 13, 15],
                    [1, 2, 5, 6, 7, 8, 9, 10],
                ],
                0,
                0,
            ),
            True,
        )

    def test_Nr14_Zadanie_152_argumenty_tablica_7_7(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [9, 8, 7, 6, 5, 4, 3, 2],
                    [1, 0, 9, 8, 7, 6, 5, 4],
                    [2, 1, 0, 9, 8, 7, 6, 5],
                    [3, 2, 1, 0, 9, 8, 7, 6],
                    [4, 3, 2, 1, 0, 9, 8, 7],
                    [5, 4, 3, 2, 1, 0, 9, 8],
                    [6, 5, 4, 3, 2, 1, 0, 9],
                    [7, 6, 5, 4, 3, 2, 1, 0],
                ],
                7,
                7,
            ),
            True,
        )

    def test_Nr15_Zadanie_152_argumenty_tablica_3_4(self):
        self.assertEqual(
            Zadanie_152(
                [
                    [3, 5, 7, 2, 4, 1, 6, 8],
                    [6, 4, 8, 1, 7, 2, 5, 3],
                    [5, 7, 6, 3, 1, 4, 8, 2],
                    [1, 2, 3, 5, 8, 6, 4, 7],
                    [7, 8, 5, 4, 6, 3, 1, 2],
                    [2, 6, 3, 7, 5, 4, 8, 1],
                    [8, 1, 2, 4, 3, 7, 6, 5],
                    [4, 3, 6, 8, 2, 5, 7, 1],
                ],
                3,
                4,
            ),
            False,
        )
