import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon73 import Zadanie_73


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

    def test_Nr01_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(30), 0.7063162427192687, places=3)

    def test_Nr02_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(20), 0.41143838358058016, places=3)

    def test_Nr03_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(25), 0.5686997039694639, places=3)

    def test_Nr04_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(31), 0.7304546337286439, places=3)

    def test_Nr05_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(35), 0.8143832388747152, places=3)

    def test_Nr06_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(39), 0.878219664366722, places=3)

    def test_Nr07_Zadanie_73(self):
            self.assertAlmostEqual(Zadanie_73(40), 0.891231809817949, places=3)


