import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon144 import Zadanie_144


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

    def test_Nr01_Zadanie_144_argumenty_tablica_30_3(self):
            self.assertEqual(Zadanie_144([2, 3, 5, 7, 11], 30, 3), 1)

    def test_Nr02_Zadanie_144_argumenty_tablica_12_2(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 6, 12], 12, 2), 3)

    def test_Nr03_Zadanie_144_argumenty_tablica_12_3(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 6, 12], 12, 3), 2)

    def test_Nr04_Zadanie_144_argumenty_tablica_24_3(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 6, 12], 24, 3), 3)

    def test_Nr05_Zadanie_144_argumenty_tablica_48_3(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 6, 12, 8], 48, 3), 4)

    def test_Nr06_Zadanie_144_argumenty_tablica_128_4(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 6, 12, 8, 16], 128, 4), 1)

    def test_Nr07_Zadanie_144_argumenty_tablica_64_3(self):
            self.assertEqual(Zadanie_144([2, 4, 8, 16], 64, 3), 1)

    def test_Nr08_Zadanie_144_argumenty_tablica_15_2(self):
            self.assertEqual(Zadanie_144([2, 3, 5, 7, 11], 15, 2), 1)

    def test_Nr09_Zadanie_144_argumenty_tablica_1_1(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 6, 12], 1, 1), 1)

    def test_Nr10_Zadanie_144_argumenty_tablica_30_3(self):
            self.assertEqual(Zadanie_144([2, 3, 5, 7, 11], 30, 3), 1)

    def test_Nr11_Zadanie_144_argumenty_tablica_1_5(self):
            self.assertEqual(Zadanie_144([1, 1, 1, 1, 1], 1, 5), 1)

    def test_Nr12_Zadanie_144_argumenty_tablica_2_6(self):
            self.assertEqual(Zadanie_144([1, 1, 1, 1, 1, 2], 2, 6), 1)

    def test_Nr13_Zadanie_144_argumenty_tablica_30_3(self):
            self.assertEqual(Zadanie_144([2, 3, 5, 10, 15, 30], 30, 3), 1)

    def test_Nr14_Zadanie_144_argumenty_tablica_16_4(self):
            self.assertEqual(Zadanie_144([2, 2, 2, 2], 16, 4), 1)

    def test_Nr15_Zadanie_144_argumenty_tablica_27_3(self):
            self.assertEqual(Zadanie_144([3, 9, 27], 27, 3), 0)

    def test_Nr16_Zadanie_144_argumenty_tablica_60_4(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 5, 6], 60, 4), 2)

    def test_Nr17_Zadanie_144_argumenty_tablica_60_4(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 5, 6], 60, 4), 2)

    def test_Nr18_Zadanie_144_argumenty_tablica_60_4(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 5, 6], 60, 4), 2)

    def test_Nr19_Zadanie_144_argumenty_tablica_36_3(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 5, 6, 7, 8, 9], 36, 3), 2)

    def test_Nr20_Zadanie_144_argumenty_tablica_20_2(self):
            self.assertEqual(Zadanie_144([2, 4, 6, 8, 10], 20, 2), 1)

    def test_Nr21_Zadanie_144_argumenty_tablica_210_4(self):
            self.assertEqual(Zadanie_144([2, 3, 5, 7, 11, 13, 17], 210, 4), 1)

    def test_Nr22_Zadanie_144_argumenty_tablica_150_3(self):
            self.assertEqual(Zadanie_144([10, 15, 20, 25, 30], 150, 3), 0)

    def test_Nr23_Zadanie_144_argumenty_tablica_45_2(self):
            self.assertEqual(Zadanie_144([1, 3, 5, 7, 9, 11, 13, 15], 45, 2), 2)

    def test_Nr24_Zadanie_144_argumenty_tablica_256_4(self):
            self.assertEqual(Zadanie_144([2, 4, 8, 16, 32, 64], 256, 4), 0)

    def test_Nr25_Zadanie_144_argumenty_tablica_48_2(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 6, 12, 24, 48], 48, 2), 2)

    def test_Nr26_Zadanie_144_argumenty_tablica_120_5(self):
            self.assertEqual(Zadanie_144([1, 2, 3, 4, 5, 6], 120, 5), 1)

    def test_Nr27_Zadanie_144_argumenty_tablica_64_4(self):
            self.assertEqual(Zadanie_144([1, 2, 4, 8, 16, 32], 64, 4), 1)

    def test_Nr28_Zadanie_144_argumenty_tablica_315_3(self):
            self.assertEqual(Zadanie_144([3, 5, 7, 9, 11, 13, 15], 315, 3), 2)

    def test_Nr29_Zadanie_144_argumenty_tablica_72_3(self):
            self.assertEqual(Zadanie_144([1, 3, 6, 12, 24, 48], 72, 3), 2)

    def test_Nr30_Zadanie_144_argumenty_tablica_231_3(self):
            self.assertEqual(Zadanie_144([2, 3, 5, 7, 11, 13], 231, 3), 1)


