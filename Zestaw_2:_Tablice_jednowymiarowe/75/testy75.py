import unittest
import os
import sys
import importlib

from szablon75 import Zadanie_75


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

    def test_Nr01_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([1, 2, 3]), True)

    def test_Nr02_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([1, 2, 3, 4, 4]), False)

    def test_Nr03_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([1, 2, 3, 4, 5, 0]), True)

    def test_Nr04_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([1, 1, 2, 3, 4, 5, 5, 6, 0]), True)

    def test_Nr05_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([1, 1, 1, 1]), False)

    def test_Nr06_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([10]), True)

    def test_Nr07_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_75(
                [999999999999999999999999999999999999, -999999999999999999999999999]
            ),
            True,
        )

    def test_Nr08_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([1, 1, 1, 1, 1, 1, 2, 0]), True)

    def test_Nr09_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_75([1000000000000, 1000000000000000000, 1000000000000]), False
        )

    def test_Nr10_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_75(
                [
                    1000000000000000000000001,
                    10000000000000000000,
                    10000000000000000000000000000009,
                ]
            ),
            True,
        )

    def test_Nr11_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([]), False)

    def test_Nr12_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_75(
                [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    1,
                    0,
                    -1,
                    -2,
                    -3,
                    -4,
                    1,
                    1,
                    1,
                    20,
                ]
            ),
            True,
        )

    def test_Nr13_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([3, 1, 4, 2]), True)

    def test_Nr14_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([2, 3, 1, 1, 4]), False)

    def test_Nr15_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(Zadanie_75([-3, -1, -2, -4]), True)

    def test_Nr16_Zadanie_75_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_75(
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]
            ),
            True,
        )
