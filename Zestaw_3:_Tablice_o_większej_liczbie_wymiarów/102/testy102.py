import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon102 import Zadanie_102


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

    def test_Nr01_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 9)

    def test_Nr02_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 211, 321], [211, 123, 122], [355, 553, 355]]), 0)

    def test_Nr03_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[112, 211, 211, 112], [211, 112, 211, 122], [112, 211, 211, 112], [122, 211, 122, 112]]), 16)

    def test_Nr04_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[11, 11], [11, 11]]), 4)

    def test_Nr05_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[355, 553, 355, 533], [553, 355, 553, 355], [355, 533, 355, 553], [533, 553, 533, 355]]), 16)

    def test_Nr06_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 345, 567, 789, 901], [234, 456, 678, 890, 123], [345, 567, 789, 564, 456], [456, 678, 890, 123, 345], [567, 789, 901, 654, 456]]), 0)

    def test_Nr07_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 345, 567, 789, 901], [234, 456, 678, 890, 123], [345, 567, 789, 564, 456], [456, 678, 890, 564, 456], [567, 789, 901, 654, 456]]), 2)

    def test_Nr08_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[112, 211, 311, 411], [211, 112, 211, 311], [311, 211, 112, 211], [411, 311, 211, 112]]), 2)

    def test_Nr09_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[10, 10], [10, 1]]), 0)

    def test_Nr10_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[122, 211, 122, 112], [211, 122, 211, 122], [122, 211, 122, 211], [112, 122, 211, 122]]), 16)

    def test_Nr11_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 355, 123, 355, 123], [355, 553, 355, 553, 355], [123, 355, 123, 355, 123], [355, 553, 355, 553, 355], [123, 355, 123, 355, 123]]), 0)


