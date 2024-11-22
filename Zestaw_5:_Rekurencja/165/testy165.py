import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon165 import Zadanie_165


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

    def test_Nr01_Zadanie_165_argumenty_tablica_4(self):
            self.assertEqual(Zadanie_165([1, 2, 3, 4, 5, 6], 4), True)

    def test_Nr02_Zadanie_165_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_165([1, 2, 3, 4, 5, 6], 10), False)

    def test_Nr03_Zadanie_165_argumenty_tablica_4(self):
            self.assertEqual(Zadanie_165([1, 1, 2, 2, 3, 3], 4), True)

    def test_Nr04_Zadanie_165_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_165([1, 2, 3], 6), False)

    def test_Nr05_Zadanie_165_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_165([2, 3, 3, 3, 3, 2], 6), True)

    def test_Nr06_Zadanie_165_argumenty_tablica_5(self):
            self.assertEqual(Zadanie_165([1, 2, 5], 5), False)

    def test_Nr07_Zadanie_165_argumenty_tablica_4(self):
            self.assertEqual(Zadanie_165([2, 4, 6, 8], 4), True)

    def test_Nr08_Zadanie_165_argumenty_tablica_6(self):
            self.assertEqual(Zadanie_165([1, 1, 1, 1, 1, 1], 6), True)

    def test_Nr09_Zadanie_165_argumenty_tablica_5(self):
            self.assertEqual(Zadanie_165([3, 3, 3, 3, 3], 5), False)

    def test_Nr10_Zadanie_165_argumenty_tablica_5(self):
            self.assertEqual(Zadanie_165([10, 20, 30, 40], 5), False)

    def test_Nr11_Zadanie_165_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_165([5, 5, 10, 10, 15], 10), False)

    def test_Nr12_Zadanie_165_argumenty_tablica_8(self):
            self.assertEqual(Zadanie_165([8, 8, 8, 8], 8), False)


