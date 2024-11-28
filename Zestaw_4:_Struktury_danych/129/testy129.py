import unittest
import os
import sys
import importlib

from szablon129 import Zadanie_129


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


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.25"), (1, 4))

    def test_Nr02_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.(6)"), (2, 3))

    def test_Nr03_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.(142857)"), (1, 7))

    def test_Nr04_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("1.25"), (5, 4))

    def test_Nr05_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.(3)"), (1, 3))

    def test_Nr06_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("1.(3)"), (4, 3))

    def test_Nr07_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.21(3)"), (16, 75))

    def test_Nr08_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.56(78)"), (937, 1650))

    def test_Nr09_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("3.7(2)"), (67, 18))

    def test_Nr10_Zadanie_129_argumenty_(self):
        self.assertEqual(Zadanie_129("0.26(9876)"), (1799, 6666))
