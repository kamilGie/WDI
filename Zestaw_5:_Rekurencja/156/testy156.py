import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon156 import Zadanie_156


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

    def test_Nr01_Zadanie_156_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_156([1, 2, 3, 4], 6), True)

    def test_Nr02_Zadanie_156_argumenty_tablica_15(self):
            self.assertEqual(Zadanie_156([3, 6, 9, 12], 15), True)

    def test_Nr03_Zadanie_156_argumenty_tablica_30(self):
            self.assertEqual(Zadanie_156([5, 10, 15, 20, 25], 30), True)

    def test_Nr04_Zadanie_156_argumenty_tablica_5(self):
            self.assertEqual(Zadanie_156([1, 5, 10, 20], 5), True)

    def test_Nr05_Zadanie_156_argumenty_tablica_8(self):
            self.assertEqual(Zadanie_156([2, 3, 5, 7, 11], 8), True)

    def test_Nr06_Zadanie_156_argumenty_tablica_55(self):
            self.assertEqual(Zadanie_156([10, 20, 30, 40, 50, 60], 55), True)

    def test_Nr07_Zadanie_156_argumenty_tablica_55(self):
            self.assertEqual(Zadanie_156([10, 20, 30, 40, 50, 60], 55), True)

    def test_Nr08_Zadanie_156_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_156([1, 2, 4, 8, 16], 10), True)

    def test_Nr09_Zadanie_156_argumenty_tablica_25(self):
            self.assertEqual(Zadanie_156([6, 8, 10, 15, 20], 25), False)

    def test_Nr10_Zadanie_156_argumenty_tablica_18(self):
            self.assertEqual(Zadanie_156([2, 4, 6, 8, 10], 18), True)

    def test_Nr11_Zadanie_156_argumenty_tablica_9(self):
            self.assertEqual(Zadanie_156([1, 3, 5, 7], 9), True)

    def test_Nr12_Zadanie_156_argumenty_tablica_30(self):
            self.assertEqual(Zadanie_156([5, 10, 15, 20, 25], 30), True)

    def test_Nr13_Zadanie_156_argumenty_tablica_15(self):
            self.assertEqual(Zadanie_156([3, 6, 9, 12], 15), True)

    def test_Nr14_Zadanie_156_argumenty_tablica_8(self):
            self.assertEqual(Zadanie_156([2, 3, 5, 7, 11], 8), True)

    def test_Nr15_Zadanie_156_argumenty_tablica_55(self):
            self.assertEqual(Zadanie_156([10, 20, 30, 40, 50, 60], 55), True)

    def test_Nr16_Zadanie_156_argumenty_tablica_25(self):
            self.assertEqual(Zadanie_156([6, 8, 10, 15, 20], 25), False)

    def test_Nr17_Zadanie_156_argumenty_tablica_18(self):
            self.assertEqual(Zadanie_156([2, 4, 6, 8, 10], 18), True)

    def test_Nr18_Zadanie_156_argumenty_tablica_9(self):
            self.assertEqual(Zadanie_156([1, 3, 5, 7], 9), True)

    def test_Nr19_Zadanie_156_argumenty_tablica_11(self):
            self.assertEqual(Zadanie_156([1, 4, 7, 8, 12], 11), False)

    def test_Nr20_Zadanie_156_argumenty_tablica_14(self):
            self.assertEqual(Zadanie_156([2, 4, 6, 9, 12], 14), True)

    def test_Nr21_Zadanie_156_argumenty_tablica_18(self):
            self.assertEqual(Zadanie_156([3, 6, 9, 12, 15], 18), True)

    def test_Nr22_Zadanie_156_argumenty_tablica_11(self):
            self.assertEqual(Zadanie_156([1, 3, 5, 6], 11), True)

    def test_Nr23_Zadanie_156_argumenty_tablica_18(self):
            self.assertEqual(Zadanie_156([7, 8, 9, 10], 18), False)

    def test_Nr24_Zadanie_156_argumenty_tablica_13(self):
            self.assertEqual(Zadanie_156([1, 2, 3, 4, 5], 13), False)


