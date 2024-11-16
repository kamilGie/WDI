import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon137 import Zadanie_137


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

    def test_Nr01_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 1, 0, 1, 1]), True)

    def test_Nr02_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 0, 1, 0, 0]), False)

    def test_Nr03_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 0, 1, 0, 1, 1, 0, 1]), True)

    def test_Nr04_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 1, 0, 1, 1, 0]), True)

    def test_Nr05_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([0, 1, 1, 1, 0, 0]), False)

    def test_Nr06_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([0, 1, 0, 0, 1, 1, 0, 0]), False)

    def test_Nr07_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), True)

    def test_Nr08_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 0, 1, 1, 0, 1]), True)

    def test_Nr09_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 0, 1, 0, 1, 1]), True)

    def test_Nr10_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([0, 1, 0, 1, 1]), True)

    def test_Nr11_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]), True)

    def test_Nr12_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0]), True)

    def test_Nr13_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1]), True)

    def test_Nr14_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1]), True)

    def test_Nr15_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]), True)

    def test_Nr16_Zadanie_137_argumenty_tablica(self):
            self.assertEqual(Zadanie_137([1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0]), True)


