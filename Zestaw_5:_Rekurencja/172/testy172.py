import unittest
import os
import sys
import importlib

from szablon172 import fibonacci


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

    def test_Nr01_fibonacci_argumenty_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_Nr02_fibonacci_argumenty_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_Nr03_fibonacci_argumenty_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_Nr04_fibonacci_argumenty_6(self):
        self.assertEqual(fibonacci(6), 8)

    def test_Nr05_fibonacci_argumenty_7(self):
        self.assertEqual(fibonacci(7), 13)

    def test_Nr06_fibonacci_argumenty_9(self):
        self.assertEqual(fibonacci(9), 34)

    def test_Nr07_fibonacci_argumenty_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_Nr08_fibonacci_argumenty_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_Nr09_fibonacci_argumenty_15(self):
        self.assertEqual(fibonacci(15), 610)

    def test_Nr10_fibonacci_argumenty_20(self):
        self.assertEqual(fibonacci(20), 6765)

    def test_Nr11_fibonacci_argumenty_40(self):
        self.assertEqual(fibonacci(40), 102334155)

    def test_Nr12_fibonacci_argumenty_50(self):
        self.assertEqual(fibonacci(50), 12586269025)

    def test_Nr13_fibonacci_argumenty_100(self):
        self.assertEqual(fibonacci(100), 354224848179261915075)
