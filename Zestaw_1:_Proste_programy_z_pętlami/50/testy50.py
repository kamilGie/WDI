import unittest
from contextlib import redirect_stdout
import io

from szablon50 import Zadanie_50


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
    import os
    import sys
    import importlib
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_50(self):
            self.assertEqual(Zadanie_50(1), 9)

    def test_Nr02_Zadanie_50(self):
            self.assertEqual(Zadanie_50(10), 14)

    def test_Nr03_Zadanie_50(self):
            self.assertEqual(Zadanie_50(14), 15)

    def test_Nr04_Zadanie_50(self):
            self.assertEqual(Zadanie_50(20), 22)

    def test_Nr05_Zadanie_50(self):
            self.assertEqual(Zadanie_50(40), 41)

    def test_Nr06_Zadanie_50(self):
            self.assertEqual(Zadanie_50(100), 101)

    def test_Nr07_Zadanie_50(self):
            self.assertEqual(Zadanie_50(512), 513)

    def test_Nr08_Zadanie_50(self):
            self.assertEqual(Zadanie_50(231), 234)

    def test_Nr09_Zadanie_50(self):
            self.assertEqual(Zadanie_50(512), 513)

    def test_Nr10_Zadanie_50(self):
            self.assertEqual(Zadanie_50(952), 954)

    def test_Nr11_Zadanie_50(self):
            self.assertEqual(Zadanie_50(999), 1000)


