import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon159 import Zadanie_159


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

    def test_Nr01_Zadanie_159_argumenty_2_3(self):
            self.assertEqual(Zadanie_159(2, 3), 3)

    def test_Nr02_Zadanie_159_argumenty_1_1(self):
            self.assertEqual(Zadanie_159(1, 1), 0)

    def test_Nr03_Zadanie_159_argumenty_3_2(self):
            self.assertEqual(Zadanie_159(3, 2), 5)

    def test_Nr04_Zadanie_159_argumenty_4_1(self):
            self.assertEqual(Zadanie_159(4, 1), 2)

    def test_Nr05_Zadanie_159_argumenty_5_0(self):
            self.assertEqual(Zadanie_159(5, 0), 0)

    def test_Nr06_Zadanie_159_argumenty_1_4(self):
            self.assertEqual(Zadanie_159(1, 4), 1)

    def test_Nr07_Zadanie_159_argumenty_3_3(self):
            self.assertEqual(Zadanie_159(3, 3), 8)

    def test_Nr08_Zadanie_159_argumenty_3_4(self):
            self.assertEqual(Zadanie_159(3, 4), 12)

    def test_Nr09_Zadanie_159_argumenty_6_3(self):
            self.assertEqual(Zadanie_159(6, 3), 48)

    def test_Nr10_Zadanie_159_argumenty_5_3(self):
            self.assertEqual(Zadanie_159(5, 3), 23)

    def test_Nr11_Zadanie_159_argumenty_3_5(self):
            self.assertEqual(Zadanie_159(3, 5), 18)

    def test_Nr12_Zadanie_159_argumenty_6_4(self):
            self.assertEqual(Zadanie_159(6, 4), 110)

    def test_Nr13_Zadanie_159_argumenty_6_6(self):
            self.assertEqual(Zadanie_159(6, 6), 434)


