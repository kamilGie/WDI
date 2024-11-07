import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon74 import fibonacci_check


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

    def test_Nr01_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 1, 1]), False)

    def test_Nr02_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([2, 1, 1]), False)

    def test_Nr03_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 6, 9, 7, 10, 11, 12, 15]), True)

    def test_Nr04_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 6, 9, 7, 5, 10, 12, 15]), False)

    def test_Nr05_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 6, 9, 10, 15, 12, 8, 21]), False)

    def test_Nr06_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 6, 4, 7]), True)

    def test_Nr07_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([4, 6, 9, 8, 10]), False)

    def test_Nr08_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([7]), True)

    def test_Nr09_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([4, 8, 9, 6, 15, 10]), False)

    def test_Nr10_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 6, 9, 7, 10, 11, 14, 15]), True)

    def test_Nr11_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 6, 9, 7, 10, 11, 13, 15, 14, 18, 16, 22, 25]), True)

    def test_Nr12_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 9, 9, 1]), False)

    def test_Nr13_fibonacci_check_argumenty_tablica(self):
            self.assertEqual(fibonacci_check([1, 4, 9, 16, 2]), True)


