import unittest
import os
import sys
import importlib

from szablon161 import Zadanie_161


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

    def test_Nr01_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([2, 3, 5, 7, 15]), True)

    def test_Nr02_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([5, 7, 15]), False)

    def test_Nr03_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([1, 3, 5, 9, 11, 13]), False)

    def test_Nr04_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([4, 8, 12, 16, 20]), False)

    def test_Nr05_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([1, 1, 2, 3, 4, 5, 6, 7]), False)

    def test_Nr06_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([6, 14, 25, 9, 18, 30]), False)

    def test_Nr07_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([2, 4, 8, 16, 32]), False)

    def test_Nr08_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([31, 7, 15, 23, 47, 63]), True)

    def test_Nr09_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([10, 14, 20, 25, 35, 40]), True)

    def test_Nr10_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([0, 1, 2, 4, 8, 16, 32]), True)

    def test_Nr11_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([1, 2, 3, 6, 9, 12, 18]), True)

    def test_Nr12_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([10, 10, 10, 10, 10, 10]), True)

    def test_Nr13_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([1, 1, 1]), True)

    def test_Nr14_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([10, 20, 30, 40, 50]), False)

    def test_Nr15_Zadanie_161_argumenty_tablica(self):
        self.assertEqual(Zadanie_161([10, 15, 20, 25, 30, 35]), True)
