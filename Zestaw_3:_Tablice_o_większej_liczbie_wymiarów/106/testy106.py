import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon106 import Zadanie_106


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

    def test_Nr01_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[23, 31, 41], [12, 15, 19], [2, 7, 3]]), True)

    def test_Nr02_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[22, 33, 44], [12, 24, 36], [5, 6, 7]]), True)

    def test_Nr03_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[5, 3, 7], [13, 5, 2], [2, 6, 9]]), True)

    def test_Nr04_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), False)

    def test_Nr05_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[17, 23, 29], [31, 37, 41], [53, 59, 67]]), True)

    def test_Nr06_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[2, 3, 5], [7, 11, 13], [17, 19, 23]]), True)

    def test_Nr07_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[10, 22, 34], [18, 25, 36], [41, 47, 53]]), False)

    def test_Nr08_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[3, 7, 9], [2, 5, 11], [13, 17, 19]]), False)

    def test_Nr09_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[3, 7, 9], [2, 5, 11], [13, 17, 19]]), False)

    def test_Nr10_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[2, 6, 10], [15, 7, 19], [12, 22, 31]]), True)

    def test_Nr11_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[5, 10, 7], [20, 15, 3], [9, 4, 2]]), True)

    def test_Nr12_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[13, 23, 33], [2, 5, 9], [7, 11, 14]]), True)

    def test_Nr13_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[2, 5, 11], [13, 17, 19], [7, 23, 29]]), True)

    def test_Nr14_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[17, 31, 13], [3, 7, 5], [2, 9, 12]]), True)

    def test_Nr15_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[3, 17, 11], [13, 2, 5], [7, 29, 19]]), True)

    def test_Nr16_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[9, 7, 5], [6, 3, 7], [10, 2, 8]]), False)

    def test_Nr17_Zadanie_106_argumenty_tablica(self):
            self.assertEqual(Zadanie_106([[7, 5, 13], [3, 23, 19], [2, 17, 29]]), True)


