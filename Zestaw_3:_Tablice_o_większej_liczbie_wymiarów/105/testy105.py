import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon105 import Zadanie_105


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

    def test_Nr01_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[22, 14], [13, 5]], [[22, 14, 10], [13, 5, 9], [15, 6, 7]]), True)

    def test_Nr02_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[22, 14], [13, 5]], [[10, 12, 9], [11, 8, 3], [6, 4, 7]]), False)

    def test_Nr03_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[22, 14], [13, 5]], [[22, 14, 9], [13, 5, 4], [6, 8, 10]]), True)

    def test_Nr04_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[22, 14], [13, 5]], [[10, 12, 9], [22, 14, 9], [13, 5, 7]]), True)

    def test_Nr05_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[10, 3], [5, 8]], [[10, 2, 5], [3, 8, 9], [4, 5, 7]]), True)

    def test_Nr06_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[1, 2], [3, 4]], [[1, 2, 5], [3, 4, 6], [5, 6, 7]]), True)

    def test_Nr07_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[1, 1], [1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]), True)

    def test_Nr08_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[7, 8], [10, 5]], [[10, 2, 7], [8, 5, 10], [3, 9, 5]]), True)

    def test_Nr09_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[15, 3], [6, 2]], [[10, 2, 5], [3, 8, 9], [5, 6, 7]]), True)

    def test_Nr10_Zadanie_105_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_105([[5, 7], [3, 9]], [[5, 7, 5], [3, 9, 3], [9, 7, 5]]), True)


