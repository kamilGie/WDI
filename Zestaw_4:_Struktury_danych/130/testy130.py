import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon130 import Zadanie_130


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

    def test_Nr01_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.25", "0.1(6)"), "0.41(6)")

    def test_Nr02_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.(3)", "0.2(7)"), "0.6(1)")

    def test_Nr03_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.5", "0.125"), "0.625")

    def test_Nr04_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.1", "0.9"), "1.0")

    def test_Nr05_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.2(3)", "0.5"), "0.7(3)")

    def test_Nr06_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.(142857)", "0.5"), "0.6(428571)")

    def test_Nr07_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.4(6)", "0.4(6)"), "0.9(3)")

    def test_Nr08_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.1(6)", "0.(6)"), "0.8(3)")

    def test_Nr09_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.3(7)", "0.3"), "0.6(7)")

    def test_Nr10_Zadanie_130(self):
        self.assertEqual(Zadanie_130("0.25", "0.25"), "0.5")
