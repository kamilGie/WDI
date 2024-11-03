import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon45 import Zadanie_45


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

    def test_Nr01_Zadanie_45_argumenty_2_1(self):
        self.assertEqual(Zadanie_45(2, 1), 4)
    def test_Nr02_Zadanie_45_argumenty_2_2(self):
        self.assertEqual(Zadanie_45(2, 2), 5)
    def test_Nr03_Zadanie_45_argumenty_2_10(self):
        self.assertEqual(Zadanie_45(2, 10), 31)
    def test_Nr04_Zadanie_45_argumenty_4_10(self):
        self.assertEqual(Zadanie_45(4, 10), 0)
    def test_Nr05_Zadanie_45_argumenty_10_4(self):
        self.assertEqual(Zadanie_45(10, 4), 11)
    def test_Nr06_Zadanie_45_argumenty_7_3(self):
        self.assertEqual(Zadanie_45(7, 3), 15)
    def test_Nr07_Zadanie_45_argumenty_123456789_10(self):
        self.assertEqual(Zadanie_45(123456789, 10), 29)
    def test_Nr08_Zadanie_45_argumenty_9876544321_12(self):
        self.assertEqual(Zadanie_45(9876544321, 12), 43)
    def test_Nr09_Zadanie_45_argumenty_2023_15(self):
        self.assertEqual(Zadanie_45(2023, 15), 78)
    def test_Nr10_Zadanie_45_argumenty_2115_10(self):
        self.assertEqual(Zadanie_45(2115, 10), 46)

