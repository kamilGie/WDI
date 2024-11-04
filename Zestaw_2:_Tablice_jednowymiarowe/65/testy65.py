import unittest
import os
import sys
import importlib

from szablon65 import list_check


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

    def test_Nr01_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([1, 1, 1]), True)

    def test_Nr02_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([135, 247, 999, 701]), True)

    def test_Nr03_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([222, 480, 600]), False)

    def test_Nr04_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([123, 456, 240]), False)

    def test_Nr05_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([7]), True)

    def test_Nr06_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([888]), False)

    def test_Nr07_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([0, 123, 1001]), False)

    def test_Nr08_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([1, 999, 1001]), True)

    def test_Nr09_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([2, 4, 6, 8, 221]), False)

    def test_Nr10_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([223, 225, 227]), True)

    def test_Nr11_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([111, 333, 555, 777, 992]), True)

    def test_Nr12_list_check_argumenty_tablica(self):
        self.assertEqual(list_check([132, 246, 357, 481]), False)
