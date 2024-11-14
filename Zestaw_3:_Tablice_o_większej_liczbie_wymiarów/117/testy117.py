import unittest
import os
import sys
import importlib

from szablon117 import Zadanie_117


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

    def test_Nr01_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(Zadanie_117([[1, 1, 2], [3, 5, 8], [5, 8, 13]]), 3)

    def test_Nr02_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117([[1, 1, 2, 3, 5], [2, 3, 5, 8, 13], [1, 1, 2, 3, 5]]), 3
        )

    def test_Nr03_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(Zadanie_117([[1, 1, 2, 3], [2, 3, 5, 8], [5, 8, 13, 21]]), 3)

    def test_Nr04_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [1, 2, 3, 5, 8, 13],
                    [4, 6, 7, 2, 9, 10],
                    [10, 15, 21, 35, 54, 89],
                    [3, 4, 5, 7, 8, 9],
                    [21, 34, 55, 89, 144, 233],
                ]
            ),
            4,
        )

    def test_Nr05_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117([[1, 3, 5, 7], [2, 4, 6, 8], [3, 5, 7, 9], [5, 8, 10, 15]]), 4
        )

    def test_Nr06_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [13, 8, 5, 3, 2, 1],
                    [4, 6, 7, 2, 9, 10],
                    [21, 34, 55, 89, 144, 233],
                    [1, 1, 1, 2, 3, 5],
                ]
            ),
            4,
        )

    def test_Nr07_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117([[5, 3, 2, 1], [8, 5, 3, 2], [13, 8, 5, 3], [21, 13, 8, 5]]), 4
        )

    def test_Nr08_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [2, 3, 5, 8, 13],
                    [10, 7, 15, 12, 21],
                    [1, 1, 2, 3, 5],
                    [21, 34, 55, 89, 144],
                ]
            ),
            3,
        )

    def test_Nr09_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [34, 55, 89, 144, 233, 377, 610, 987, 1597],
                    [55, 89, 144, 233, 377, 610, 987, 1597, 2584],
                    [233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],
                    [377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711],
                    [610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657],
                    [987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368],
                    [1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025],
                    [2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393],
                    [4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418],
                ]
            ),
            7,
        )

    def test_Nr10_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [13, 8, 5, 3, 2, 1],
                    [4, 6, 7, 2, 9, 10],
                    [21, 34, 55, 89, 144, 233],
                    [1, 1, 1, 2, 3, 5],
                ]
            ),
            4,
        )

    def test_Nr11_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [1, 2, 4, 6, 10],
                    [2, 4, 6, 9, 14],
                    [3, 5, 8, 13, 21],
                    [13, 21, 34, 55, 89],
                ]
            ),
            3,
        )

    def test_Nr12_Zadanie_117_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_117(
                [
                    [1, 1, 2, 3, 5, 8, 13],
                    [4, 6, 10, 16, 26, 42, 68],
                    [2, 4, 6, 9, 15, 24, 39],
                    [21, 34, 55, 89, 144, 233, 377],
                ]
            ),
            5,
        )
