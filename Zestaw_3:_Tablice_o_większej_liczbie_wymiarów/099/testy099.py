import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon099 import geometric_series


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

    def test_Nr01_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series([[2, 4, 8, 16], [3, 2, 4, 8], [5, 3, 2, 4], [7, 5, 3, 2]]),
            4,
        )

    def test_Nr02_geometric_series_argumenty_tablica(self):
        self.assertEqual(geometric_series([[1, 3, 9], [2, 6, 18], [4, 12, 36]]), 3)

    def test_Nr03_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series([[10, 20, 30], [5, 15, 25], [1, 2, 3]]), False
        )

    def test_Nr04_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series(
                [[1, 2, 4, 8], [1, 3, 9, 27], [1, 4, 16, 64], [2, 8, 32, 128]]
            ),
            False,
        )

    def test_Nr05_geometric_series_argumenty_tablica(self):
        self.assertEqual(geometric_series([[1, 2], [3, 6]]), False)

    def test_Nr06_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series([[2, 4, 8, 16], [3, 2, 4, 8], [5, 3, 2, 4], [7, 5, 3, 2]]),
            4,
        )

    def test_Nr07_geometric_series_argumenty_tablica(self):
        self.assertEqual(geometric_series([[1, 3, 9], [2, 6, 18], [4, 12, 36]]), 3)

    def test_Nr08_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series([[10, 20, 30], [5, 15, 25], [1, 2, 3]]), False
        )

    def test_Nr09_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series(
                [[1, 2, 4, 8], [1, 3, 9, 27], [1, 4, 16, 64], [2, 8, 32, 128]]
            ),
            False,
        )

    def test_Nr11_geometric_series_argumenty_tablica(self):
        self.assertEqual(geometric_series([[2, 6, 18], [1, 3, 9], [1, 2, 4]]), False)

    def test_Nr12_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series(
                [[2, 6, 18, 54], [1, 3, 9, 27], [5, 15, 45, 135], [3, 9, 27, 81]]
            ),
            False,
        )

    def test_Nr13_geometric_series_argumenty_tablica(self):
        self.assertEqual(
            geometric_series(
                [
                    [1, 3, 9, 27, 81],
                    [1, 2, 4, 8, 16],
                    [5, 10, 20, 40, 80],
                    [2, 4, 8, 16, 32],
                    [1, 5, 25, 125, 625],
                ]
            ),
            False,
        )

    def test_Nr14_geometric_series_argumenty_tablica(self):
        self.assertEqual(geometric_series([[1]]), False)
