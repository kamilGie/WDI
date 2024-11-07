import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon61 import same_digits


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

    def test_Nr01_same_digits_argumenty_123_321(self):
        self.assertEqual(same_digits(123, 321), True)
    def test_Nr02_same_digits_argumenty_1255_5125(self):
        self.assertEqual(same_digits(1255, 5125), True)
    def test_Nr03_same_digits_argumenty_11000_10001(self):
        self.assertEqual(same_digits(11000, 10001), True)
    def test_Nr04_same_digits_argumenty_112233_332211(self):
        self.assertEqual(same_digits(112233, 332211), True)
    def test_Nr05_same_digits_argumenty_123456_654321(self):
        self.assertEqual(same_digits(123456, 654321), True)
    def test_Nr06_same_digits_argumenty_1234_43210(self):
        self.assertEqual(same_digits(1234, 43210), False)
    def test_Nr07_same_digits_argumenty_987_7890(self):
        self.assertEqual(same_digits(987, 7890), False)
    def test_Nr08_same_digits_argumenty_1000_1(self):
        self.assertEqual(same_digits(1000, 1), False)
    def test_Nr09_same_digits_argumenty_100_1(self):
        self.assertEqual(same_digits(100, 1), False)
    def test_Nr10_same_digits_argumenty_7_7(self):
        self.assertEqual(same_digits(7, 7), True)
    def test_Nr11_same_digits_argumenty_5_3(self):
        self.assertEqual(same_digits(5, 3), False)
    def test_Nr12_same_digits_argumenty_0_0(self):
        self.assertEqual(same_digits(0, 0), True)
    def test_Nr13_same_digits_argumenty_0_1000(self):
        self.assertEqual(same_digits(0, 1000), False)
    def test_Nr14_same_digits_argumenty_1410_4101(self):
        self.assertEqual(same_digits(1410, 4101), True)
    def test_Nr15_same_digits_argumenty_123456789_987654321(self):
        self.assertEqual(same_digits(123456789, 987654321), True)
    def test_Nr16_same_digits_argumenty_1234567890987654321_987654321234567890(self):
        self.assertEqual(same_digits(1234567890987654321, 987654321234567890), False)
    def test_Nr17_same_digits_argumenty_123123123_321321312(self):
        self.assertEqual(same_digits(123123123, 321321312), True)
    def test_Nr18_same_digits_argumenty_2115_2004(self):
        self.assertEqual(same_digits(2115, 2004), False)

