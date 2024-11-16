import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon140 import Zadanie_140


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

    def test_Nr01_Zadanie_140_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_140([1, 2, 3, 4, 5], 6), True)

    def test_Nr02_Zadanie_140_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_140([1, 2, 3, 4, 5], 10), True)

    def test_Nr03_Zadanie_140_argumenty_tablica_7(self):
            self.assertEqual(Zadanie_140([2, 4, 6, 8], 7), False)

    def test_Nr04_Zadanie_140_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_140([3, 7, 2, 5], 10), True)

    def test_Nr05_Zadanie_140_argumenty_tablica_17(self):
            self.assertEqual(Zadanie_140([3, 7, 2, 5], 17), True)

    def test_Nr06_Zadanie_140_argumenty_tablica_25(self):
            self.assertEqual(Zadanie_140([10, 20, 30], 25), False)

    def test_Nr07_Zadanie_140_argumenty_tablica_30(self):
            self.assertEqual(Zadanie_140([10, 20, 30], 30), True)

    def test_Nr08_Zadanie_140_argumenty_tablica_5(self):
            self.assertEqual(Zadanie_140([1, 2, 4, 8, 16, 32], 5), True)

    def test_Nr09_Zadanie_140_argumenty_tablica_17(self):
            self.assertEqual(Zadanie_140([7, 11, 13, 17], 17), True)

    def test_Nr10_Zadanie_140_argumenty_tablica_11(self):
            self.assertEqual(Zadanie_140([3, 6, 9, 12], 11), False)

    def test_Nr11_Zadanie_140_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_140([8, 4, 3, 7, 2], 10), True)

    def test_Nr12_Zadanie_140_argumenty_tablica_22(self):
            self.assertEqual(Zadanie_140([1, 2, 4, 8, 16, 32, 64], 22), True)


