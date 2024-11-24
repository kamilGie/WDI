import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon124 import Zadanie_124


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


import unittest


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_124_argumenty_tablica(self):
        self.assertEqual(Zadanie_124([(1, 1), (-1, -1), (-1, 1), (1, -1)]), True)

    def test_Nr02_Zadanie_124_argumenty_tablica(self):
        self.assertEqual( Zadanie_124([(0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1), (1, 0)]), True)

    def test_Nr03_Zadanie_124_argumenty_tablica(self):
        self.assertEqual( Zadanie_124([(0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, 0)]), False)

    def test_Nr04_Zadanie_124_argumenty_tablica(self):
        self.assertEqual(Zadanie_124([(-2, -2), (2, 2), (2, -2), (-2, 2)]), True)

    def test_Nr05_Zadanie_124_argumenty_tablica(self):
        self.assertEqual(Zadanie_124([(-2, -2), (2, 2), (3, -2), (-2, 2)]), False)

    def test_Nr06_Zadanie_124_argumenty_tablica(self):
        self.assertEqual(Zadanie_124([(-2, -2), (2, 2), (2, -3), (-2, 2)]), False)

    def test_Nr07_Zadanie_124_argumenty_tablica(self):
        self.assertEqual( Zadanie_124([(-2, -2), (2, 2), (2, -2), (-2, 2), (0, 0)]), False)

    def test_Nr08_Zadanie_124_argumenty_tablica(self):
        self.assertEqual( Zadanie_124([(-5, -5), (-5, 5), (5, -5), (5, 5), (5, -2)]), True)

    def test_Nr09_Zadanie_124_argumenty_tablica(self):
        self.assertEqual( Zadanie_124([(-5, -5), (-5, 5), (5, -5), (5, 5), (4, 4)]), False)

    def test_Nr10_Zadanie_124_argumenty_tablica(self):
        self.assertEqual( Zadanie_124([(-5, -5), (-5, 5), (5, -5), (5, 5), (5, 1), (5, 2), (5, 3)]), True,)


if __name__ == "__main__":
    unittest.main()
