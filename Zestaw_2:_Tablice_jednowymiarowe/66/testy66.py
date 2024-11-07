import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon66 import list_check


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

    def test_Nr01_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([123, 135, 579, 246]), True)
    def test_Nr02_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([248, 462, 680]), False)
    def test_Nr03_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([135]), True)
    def test_Nr04_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([1357, 246, 5792]), True)
    def test_Nr05_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([]), False)
    def test_Nr06_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([7, 248, 462]), True)
    def test_Nr07_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([4, 248, 462]), False)
    def test_Nr08_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([2, 4, 6, 8, 246, 462]), False)
    def test_Nr09_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([2, 4, 6, 8, 246, 1]), True)
    def test_Nr10_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([999]), True)
    def test_Nr11_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([13579, 888, 246, 1111]), True)
    def test_Nr12_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([86420, 480246, 1024, 6886]), False)
    def test_Nr13_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([135, 579, 97531, 7531]), True)
    def test_Nr14_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([135791357913579, 246824682468, 13579]), True)
    def test_Nr15_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([1, 22, 333, 4444, 55555]), True)
    def test_Nr16_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([1, 3, 5, 7, 9]), True)
    def test_Nr17_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([12, 23, 456, 135]), True)
    def test_Nr18_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([1312, 9753, 2468]), True)
    def test_Nr19_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([135, 135, 246, 135]), True)

