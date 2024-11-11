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
            self.assertEqual(Zadanie_102([[123, 321], [211, 122]]), 0)

    def test_Nr02_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 321, 431], [122, 211, 122], [355, 3553, 35]]), 0)

    def test_Nr03_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 456], [789, 111]]), 0)

    def test_Nr04_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 321], [456, 654]]), 0)

    def test_Nr05_Zadanie_102_argumenty_tablica(self):
            self.assertEqual(Zadanie_102([[123, 321, 211], [122, 122, 211], [321, 123, 123]]), 0)


