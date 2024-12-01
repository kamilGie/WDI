import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon168 import divide


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

    def test_Nr01_divide_argumenty_273(self):
            self.assertEqual(divide(273), True)

    def test_Nr02_divide_argumenty_22222(self):
            self.assertEqual(divide(22222), True)

    def test_Nr03_divide_argumenty_23672(self):
            self.assertEqual(divide(23672), True)

    def test_Nr04_divide_argumenty_2222(self):
            self.assertEqual(divide(2222), False)

    def test_Nr05_divide_argumenty_21722(self):
            self.assertEqual(divide(21722), False)

    def test_Nr06_divide_argumenty_3137(self):
            self.assertEqual(divide(3137), True)

    def test_Nr07_divide_argumenty_29(self):
            self.assertEqual(divide(29), False)

    def test_Nr08_divide_argumenty_27(self):
            self.assertEqual(divide(27), True)

    def test_Nr09_divide_argumenty_883(self):
            self.assertEqual(divide(883), False)

    def test_Nr10_divide_argumenty_8191(self):
            self.assertEqual(divide(8191), False)

    def test_Nr11_divide_argumenty_7437432(self):
            self.assertEqual(divide(7437432), True)

    def test_Nr12_divide_argumenty_7437439(self):
            self.assertEqual(divide(7437439), True)


