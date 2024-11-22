import unittest
import os
import sys
import importlib

from szablon153 import Zadanie_153


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

    def test_Nr01_Zadanie_153_argumenty_0_1_tablica(self):
        self.assertEqual(
            Zadanie_153(
                0,
                1,
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
            ),
            [1, 1, 3, 1, 1, 2, 0, 1, 0],
        )

    def test_Nr07_Zadanie_153_argumenty_1_1_tablica(self):
        self.assertEqual(
            Zadanie_153(
                1,
                1,
                [
                    [9, 4, 6, 2, 3, 5, 35, 8],
                    [1, 5, 7, 2, 4, 6, 36, 9],
                    [2, 6, 8, 3, 5, 7, 37, 10],
                    [3, 7, 9, 4, 6, 8, 38, 11],
                    [4, 8, 10, 5, 7, 9, 39, 12],
                    [5, 9, 11, 6, 8, 10, 40, 13],
                    [6, 10, 12, 7, 9, 11, 41, 14],
                    [7, 11, 13, 8, 10, 12, 42, 15],
                ],
            ),
            [5],
        )

    def test_Nr13_Zadanie_153_argumenty_0_1_tablica(self):
        self.assertEqual(
            Zadanie_153(
                0,
                1,
                [
                    [1, 1, 2, 2, 2, 3, 3, 3],
                    [1, 2, 3, 3, 4, 5, 5, 6],
                    [2, 3, 4, 4, 5, 6, 6, 7],
                    [3, 4, 5, 5, 6, 7, 7, 8],
                    [4, 5, 6, 6, 7, 8, 8, 9],
                    [5, 6, 7, 7, 8, 9, 9, 10],
                    [6, 7, 8, 8, 9, 10, 10, 11],
                    [7, 8, 9, 9, 10, 11, 11, 12],
                ],
            ),
            [0, 0, 0, 0, 0, 0],
        )
