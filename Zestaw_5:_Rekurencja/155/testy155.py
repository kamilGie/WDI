import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon155 import Zadanie_155


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

    def test_Nr01_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([2, 3, 5, 7, 11, 13]), -1)

    def test_Nr02_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([4, 6, 8, 10, 12]), 2)

    def test_Nr03_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([7]), 0)

    def test_Nr04_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([5, 2, 3, 6, 7, 11, 13]), -1)

    def test_Nr05_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([10, 15, 20, 25, 30]), 2)

    def test_Nr06_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([3, 6, 9, 2, 5, 7, 11, 13]), -1)

    def test_Nr07_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([1, 1, 1, 1]), -1)

    def test_Nr08_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([100, 200, 300, 400]), -1)

    def test_Nr09_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([2, 3, 5, 7, 11, 13]), -1)

    def test_Nr10_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([17, 9, 4, 3, 11, 5, 13]), -1)

    def test_Nr11_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([2, 5, 11, 17, 23, 29, 31]), -1)

    def test_Nr12_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([4, 8, 16, 32, 64, 128]), -1)

    def test_Nr13_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([2, 3, 5, 7, 11, 13]), -1)

    def test_Nr14_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([5, 2, 6, 5, 11]), -1)

    def test_Nr15_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), -1)

    def test_Nr16_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([6, 2, 9, 8, 7, 3]), 2)

    def test_Nr17_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([4, 6, 9, 2, 8, 11]), 2)

    def test_Nr18_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([15, 2, 4, 9, 11, 7]), 1)

    def test_Nr19_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([2, 3, 5, 7, 11, 13]), -1)

    def test_Nr20_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([6, 4, 9, 2, 10, 7, 11, 13, 17]), -1)

    def test_Nr21_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([12, 14, 16, 18, 20]), 2)

    def test_Nr22_Zadanie_155_argumenty_tablica(self):
            self.assertEqual(Zadanie_155([10, 14, 21, 8, 26]), -1)


