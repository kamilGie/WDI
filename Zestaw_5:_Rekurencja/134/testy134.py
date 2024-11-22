import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon134 import Zadanie_134


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

    def test_Nr01_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([6, 10, 15, 30, 64]), True)

    def test_Nr02_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([2, 3, 5, 7, 11]), True)

    def test_Nr03_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([8, 9, 27, 36, 54]), False)

    def test_Nr04_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([12, 18, 24, 36]), True)

    def test_Nr05_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([10, 15, 25, 30]), False)

    def test_Nr06_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([4, 6, 9, 16, 25]), False)

    def test_Nr07_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([1, 6, 12, 18]), False)

    def test_Nr08_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([2, 3, 5, 7, 11, 13]), True)

    def test_Nr09_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([8, 8, 9, 9, 9]), False)

    def test_Nr10_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([30, 18, 9, 12, 36, 54]), False)

    def test_Nr11_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([2, 4, 8, 16, 32]), True)

    def test_Nr12_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([6, 10, 14, 15]), False)

    def test_Nr13_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([9, 27, 81, 243]), False)

    def test_Nr14_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([6, 12, 18, 36]), True)

    def test_Nr15_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([25, 50, 75, 100, 150]), False)

    def test_Nr16_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([2, 3, 5, 7, 11, 13, 17, 19]), True)

    def test_Nr17_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([1, 3, 6, 9, 12]), True)

    def test_Nr18_Zadanie_134_argumenty_tablica(self):
            self.assertEqual(Zadanie_134([2, 3, 5, 7, 11, 13, 17]), True)


