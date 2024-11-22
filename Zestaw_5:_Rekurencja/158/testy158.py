import unittest
import os
import sys
import importlib

from szablon158 import Zadanie_158


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

    def test_Nr04_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([30, 18, 20, 6, 25]), 2)

    def test_Nr06_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([3, 6, 9, 12]), -1)

    def test_Nr08_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([10, 20, 30, 40, 50]), 2)

    def test_Nr10_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([6, 9, 12, 18, 24]), 2)

    def test_Nr12_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([3, 4, 6, 8, 10]), -1)

    def test_Nr14_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([6, 8, 9, 12]), 1)

    def test_Nr18_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([15, 25, 35, 50]), 1)

    def test_Nr22_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([30, 18, 20, 6, 25]), 2)

    def test_Nr23_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([11, 13, 17, 19]), -1)

    def test_Nr25_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([10, 20, 30, 40, 50]), 2)

    def test_Nr26_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([6, 9, 12, 18, 24]), 2)

    def test_Nr30_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([15, 25, 35, 50]), 1)

    def test_Nr32_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([2, 4, 6, 8, 9, 10]), -1)

    def test_Nr33_Zadanie_158_argumenty_tablica(self):
        self.assertEqual(Zadanie_158([15, 25, 35, 50]), 1)
