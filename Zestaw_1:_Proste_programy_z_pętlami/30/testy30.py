import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon30 import pole


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

    def test_Nr01_pole(self):
            self.assertAlmostEqual(pole(1), 0, places=3)

    def test_Nr02_pole(self):
            self.assertAlmostEqual(pole(2), 0.693222181184967, places=3)

    def test_Nr03_pole(self):
            self.assertAlmostEqual(pole(5), 1.6094779132335866, places=3)

    def test_Nr04_pole(self):
            self.assertAlmostEqual(pole(10), 2.302640093818823, places=3)

    def test_Nr05_pole(self):
            self.assertAlmostEqual(pole(20), 2.9957847743859816, places=3)

    def test_Nr06_pole(self):
            self.assertAlmostEqual(pole(40), 3.6889282049478695, places=3)

    def test_Nr07_pole(self):
            self.assertAlmostEqual(pole(50), 3.912072006260377, places=3)

    def test_Nr08_pole(self):
            self.assertAlmostEqual(pole(100), 4.605219686808785, places=3)

    def test_Nr09_pole(self):
            self.assertAlmostEqual(pole(10000), 9.21039037679036, places=3)


