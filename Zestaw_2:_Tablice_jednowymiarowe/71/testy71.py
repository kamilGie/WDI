import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon71 import Zadanie_71


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

    def test_Nr01_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1]), (1, 1))

    def test_Nr02_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1,3]), (2, 2))

    def test_Nr03_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1, 3, 5, 2, 1, 7]), (3, 2))

    def test_Nr04_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1, 3, 5, 7, 9, 11, 13]), (7, 1))

    def test_Nr05_Zadanie_71(self):
            self.assertEqual(Zadanie_71([13, 11, 9, 7, 5, 3, 1]), (1, 7))

    def test_Nr06_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1, 3, 1, 3, 1, 3]), (2, 2))

    def test_Nr07_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1, 3, 5, 7, 9, 11, 13, 15, 17]), (9, 1))

    def test_Nr08_Zadanie_71(self):
            self.assertEqual(Zadanie_71([1, 99, 3, 97, 5, 95, 7, 93]), (2, 2))


