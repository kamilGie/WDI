import unittest
import os
import sys
import importlib

from szablon118 import Zadanie_118


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

    def test_Nr01_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 1, 2])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set( tuple(x) if isinstance(x, list) else x for x in (1, 2))  # tu jest oczekiwany wynik np (1,2)
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr02_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[10, 15, 20, 25], [30, 35, 40, 45], [50, 55, 60, 65], [70, 75, 80, 85]],
            [3, 2, 1, 0],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 1))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr03_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[5, 1, 3], [2, 8, 6], [4, 7, 9]], [2, 0, 1])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 1))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr04_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[100, 200, 300], [400, 500, 600], [700, 800, 900]], [0, 2, 1]
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (1, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr05_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]], [0, 1, 2, 3]
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (2, 3))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr06_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24], [26, 28, 30, 32]],
            [3, 1, 0, 2],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 3))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr07_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23], [25, 27, 29, 31]],
            [0, 3, 2, 1],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (1, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr08_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[8, 6, 4, 2], [16, 14, 12, 10], [24, 22, 20, 18], [32, 30, 28, 26]],
            [1, 0, 3, 2],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (2, 3))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr09_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[9, 8, 7], [6, 5, 4], [3, 2, 1]], [1, 0, 2])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 1))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr10_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[50, 45, 40], [35, 30, 25], [20, 15, 10]], [2, 1, 0])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (1, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr11_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[50, 45, 40], [35, 30, 25], [20, 15, 10]], [2, 1, 0])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (1, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr12_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[50, 45, 40], [35, 30, 25], [20, 15, 10]], [2, 1, 0])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (1, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr13_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [
                [30, 60, 90, 120],
                [150, 180, 210, 240],
                [270, 300, 330, 360],
                [390, 420, 450, 480],
            ],
            [3, 2, 1, 0],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 1))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr14_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[10, 20, 30], [40, 50, 60], [70, 80, 90]], [2, 0, 1])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr15_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[5, 3, 1], [7, 5, 3], [9, 7, 5]], [2, 1, 0])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 1))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr16_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48]],
            [0, 3, 2, 1],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (1, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr17_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[2, 4], [6, 8]], [0, 1])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 1))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr18_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118([[2, 4, 6], [8, 10, 12], [14, 16, 18]], [1, 0, 2])
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (0, 2))
        self.assertTrue(wynik == oczekiwany_wynik)

    def test_Nr19_Zadanie_118_argumenty_tablica_tablica(self):
        wynik = Zadanie_118(
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [0, 2, 3, 1, 4],
        )
        wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
        oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in (2, 4))
        self.assertTrue(wynik == oczekiwany_wynik)
