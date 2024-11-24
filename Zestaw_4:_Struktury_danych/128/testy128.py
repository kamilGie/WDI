import unittest
import os
import sys
import importlib

from szablon128 import distance


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

    def test_Nr01_distance_argumenty_tablica(self):
        self.assertEqual(distance([[1, 1], [1, 0]]), 1)

    def test_Nr02_distance_argumenty_tablica(self):
        self.assertEqual(
            distance([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 0, 0]]), 7
        )

    def test_Nr03_distance_argumenty_tablica(self):
        self.assertEqual(
            distance([[1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]), 9
        )

    def test_Nr04_distance_argumenty_tablica(self):
        self.assertEqual(distance([[1, 0, 1], [1, 1, 0], [0, 0, 1]]), 5)

    def test_Nr05_distance_argumenty_tablica(self):
        self.assertEqual(
            distance(
                [
                    [0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 0, 1, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1],
                    [0, 1, 1, 1, 0, 0, 1],
                    [1, 0, 1, 1, 0, 1, 0],
                ]
            ),
            57,
        )

    def test_Nr06_distance_argumenty_tablica(self):
        self.assertEqual(
            distance(
                [
                    [1, 0, 1, 1, 1, 0, 0, 1],
                    [0, 1, 0, 1, 0, 1, 1, 0],
                    [1, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1],
                    [1, 1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1],
                ]
            ),
            195,
        )

    def test_Nr07_distance_argumenty_tablica(self):
        self.assertEqual(
            distance(
                [
                    [1, 0, 1, 1, 0, 0, 1, 0],
                    [0, 1, 0, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 0, 0, 0, 1],
                    [0, 0, 1, 0, 1, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1, 0, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0],
                    [1, 0, 0, 1, 1, 0, 0, 1],
                ]
            ),
            166,
        )

    def test_Nr08_distance_argumenty_tablica(self):
        self.assertEqual(
            distance(
                [
                    [1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 1, 0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 1, 0, 0, 1, 0],
                    [1, 1, 1, 0, 0, 1, 0, 0, 1],
                    [1, 0, 1, 0, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0, 1, 0, 0],
                ]
            ),
            279,
        )

    def test_Nr09_distance_argumenty_tablica(self):
        self.assertEqual(
            distance(
                [
                    [0, 1, 0, 0, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 0, 0, 1, 0, 1],
                    [0, 1, 1, 0, 1, 0, 1, 1, 0],
                    [1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 1, 1, 1, 1, 0],
                ]
            ),
            278,
        )

    def test_Nr10_distance_argumenty_tablica(self):
        self.assertEqual(
            distance(
                [
                    [1, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 1, 1, 1, 0, 0],
                    [1, 0, 1, 0, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 0, 0, 1, 0, 0, 1, 1],
                    [0, 1, 1, 1, 0, 1, 0, 0, 1],
                    [1, 0, 0, 1, 0, 1, 1, 0, 1],
                ]
            ),
            231,
        )
