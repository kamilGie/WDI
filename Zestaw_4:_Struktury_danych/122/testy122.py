import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon122 import Zadanie_122


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[26, 5], [2, 4]]), True)

    def test_Nr02_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[87, 1], [3, 4], [1, 6]]), False)

    def test_Nr03_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 2], [2, 4], [3, 6]]), True)

    def test_Nr04_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 0], [2, 0]]), False)

    def test_Nr05_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [0, 1], [0, 2]]), False)

    def test_Nr06_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 1], [2, 2]]), False)

    def test_Nr07_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 2], [2, 3]]), False)

    def test_Nr08_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([]), True)

    def test_Nr09_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20], [11, 22], [12, 24], [13, 26], [14, 28], [15, 30], [16, 32], [17, 34], [18, 36], [19, 38], [20, 40], [21, 42], [22, 44], [23, 46], [24, 48], [25, 50], [26, 52], [27, 54], [28, 56], [29, 58], [30, 60], [31, 62], [32, 64], [33, 66], [34, 68], [35, 70], [36, 72], [37, 74], [38, 76], [39, 78], [40, 80], [41, 82], [42, 84], [43, 86], [44, 88], [45, 90], [46, 92], [47, 94], [48, 96], [49, 98], [50, 1], [51, 3], [52, 5], [53, 7], [54, 9], [55, 11], [56, 13], [57, 15], [58, 17], [59, 19], [60, 21], [61, 23], [62, 25], [63, 27], [64, 29], [65, 31], [66, 33], [67, 35], [68, 37], [69, 39], [70, 41], [71, 43], [72, 45], [73, 47], [74, 49], [75, 51], [76, 53], [77, 55], [78, 57], [79, 59], [80, 61], [81, 63], [82, 65], [83, 67], [84, 69], [85, 71], [86, 73], [87, 75], [88, 77], [89, 79], [90, 81], [91, 83], [92, 85], [93, 87], [94, 89], [95, 91], [96, 93], [97, 95], [98, 97], [99, 99]]), False)

    def test_Nr10_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]), False)

    def test_Nr11_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 1], [2, 3], [3, 5], [4, 7]]), False)

    def test_Nr12_Zadanie_122_argumenty_tablica(self):
            self.assertEqual(Zadanie_122([[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18]]), True)


