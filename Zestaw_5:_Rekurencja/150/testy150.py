import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon150 import new_number_prime


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

    def test_Nr01_new_number_prime_argumenty_123_75(self):
            self.assertEqual(new_number_prime(123, 75), 0)

    def test_Nr02_new_number_prime_argumenty_1_1(self):
            self.assertEqual(new_number_prime(1, 1), 2)

    def test_Nr03_new_number_prime_argumenty_4_6(self):
            self.assertEqual(new_number_prime(4, 6), 0)

    def test_Nr04_new_number_prime_argumenty_2_3(self):
            self.assertEqual(new_number_prime(2, 3), 1)

    def test_Nr05_new_number_prime_argumenty_11_11(self):
            self.assertEqual(new_number_prime(11, 11), 0)

    def test_Nr06_new_number_prime_argumenty_123_456(self):
            self.assertEqual(new_number_prime(123, 456), 0)

    def test_Nr07_new_number_prime_argumenty_101_7(self):
            self.assertEqual(new_number_prime(101, 7), 0)

    def test_Nr08_new_number_prime_argumenty_19_23(self):
            self.assertEqual(new_number_prime(19, 23), 0)

    def test_Nr09_new_number_prime_argumenty_111_222(self):
            self.assertEqual(new_number_prime(111, 222), 0)

    def test_Nr10_new_number_prime_argumenty_5_3(self):
            self.assertEqual(new_number_prime(5, 3), 1)

    def test_Nr11_new_number_prime_argumenty_17_31(self):
            self.assertEqual(new_number_prime(17, 31), 0)

    def test_Nr12_new_number_prime_argumenty_13_2(self):
            self.assertEqual(new_number_prime(13, 2), 0)

    def test_Nr13_new_number_prime_argumenty_19_7(self):
            self.assertEqual(new_number_prime(19, 7), 3)

    def test_Nr14_new_number_prime_argumenty_11_3(self):
            self.assertEqual(new_number_prime(11, 3), 3)

    def test_Nr15_new_number_prime_argumenty_7_13(self):
            self.assertEqual(new_number_prime(7, 13), 2)

    def test_Nr16_new_number_prime_argumenty_17_2(self):
            self.assertEqual(new_number_prime(17, 2), 1)

    def test_Nr17_new_number_prime_argumenty_5_13(self):
            self.assertEqual(new_number_prime(5, 13), 0)


