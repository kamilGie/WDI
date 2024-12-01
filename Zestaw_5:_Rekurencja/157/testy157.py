import unittest
import os
import sys
import importlib

from szablon157 import Zadanie_157


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

    def test_Nr01_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 0), (0, 1), (1, 1)]), 0.23570226039551578, places=2
        )

    def test_Nr03_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(0, 0), (2, 0), (2, 2), (0, 2)]), 0.0, places=2
        )

    def test_Nr04_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(0, 0), (1, 1), (2, 2), (3, 3)]), 0.0, places=2
        )

    def test_Nr05_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(0, 0), (1, 2), (3, 4), (5, 6)]), 0.0, places=2
        )

    def test_Nr06_Zadanie_157(self):
        self.assertAlmostEqual(Zadanie_157([(1, 1), (2, 2), (3, 3)]), 0.0, places=2)

    def test_Nr07_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 1), (2, 2)]), 0.7071067811865476, places=2
        )

    def test_Nr08_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 0), (0, 1), (1, 1)]), 0.23570226039551578, places=2
        )

    def test_Nr09_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(0, 0), (1, 0), (0, 1), (1, 1)]), 0.0, places=2
        )

    def test_Nr10_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 2), (3, 4), (5, 6), (7, 8)]), 0.0, places=2
        )

    def test_Nr11_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]), 0.0, places=2
        )

    def test_Nr12_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 2), (21, 5), (51, 8), (14, 10), (12, 15)]),
            0.4859126579037753,
            places=2,
        )

    def test_Nr13_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157([(1, 0), (21, 5), (1, 8), (14, 10), (12, 15)]),
            0.16666666666666696,
            places=2,
        )

    def test_Nr14_Zadanie_157(self):
        self.assertAlmostEqual(
            Zadanie_157(
                [(1000, 1001), (2000, 2003), (3000, 3002), (4300, 4400), (5200, 5100)]
            ),
            0.5,
            places=2,
        )
