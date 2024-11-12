import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon097 import Zadanie_97


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

    def test_Nr01_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[1, 3, 5], [2, 4, 6], [7, 8, 9]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_Nr02_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[1, 2, 2], [3, 4, 4], [5, 5, 6]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 6, 0, 0, 0])

    def test_Nr03_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[2, 2, 3], [3, 4, 4], [5, 5, 5]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [2, 3, 4, 5, 0, 0, 0, 0, 0])

    def test_Nr04_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_Nr05_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[1, 1, 2], [2, 3, 4], [5, 5, 6]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 6, 0, 0, 0])

    def test_Nr06_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[1, 2, 2], [1, 3, 4], [4, 5, 6]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 6, 0, 0, 0])

    def test_Nr07_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[-1, 2, 3], [4, -5, 6], [7, 8, -9]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [2, 3, 4, -5, 6, 7, 8, -9, 0])

    def test_Nr08_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[1, 2, 2], [1, 3, 3], [4, 4, 5]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [1, 2, 3, 4, 5, 0, 0, 0, 0])

    def test_Nr09_Zadanie_97_argumenty_tablica_tablica(self):
            self.assertEqual(Zadanie_97([[100, 200, 300], [400, 500, 600], [700, 800, 900]], [0, 0, 0, 0, 0, 0, 0, 0, 0]), [100, 200, 300, 400, 500, 600, 700, 800, 900])


