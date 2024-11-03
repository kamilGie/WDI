import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon31 import czy_ciag


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

    def test_Nr01_czy_ciag_argumenty_2(self):
        wynik  = czy_ciag(2)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_czy_ciag_argumenty_7(self):
        wynik  = czy_ciag(7)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_czy_ciag_argumenty_20(self):
        wynik  = czy_ciag(20)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_czy_ciag_argumenty_1(self):
        wynik  = czy_ciag(1)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_czy_ciag_argumenty_10(self):
        wynik  = czy_ciag(10)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_czy_ciag_argumenty_100(self):
        wynik  = czy_ciag(100)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_czy_ciag_argumenty_1002(self):
        wynik  = czy_ciag(1002)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_czy_ciag_argumenty_5(self):
        wynik  = czy_ciag(5)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_czy_ciag_argumenty_101(self):
        wynik  = czy_ciag(101)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_czy_ciag_argumenty_123(self):
        wynik  = czy_ciag(123)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_czy_ciag_argumenty_1409(self):
        wynik  = czy_ciag(1409)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_czy_ciag_argumenty_0(self):
        wynik  = czy_ciag(0)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_czy_ciag_argumenty_2115(self):
        wynik  = czy_ciag(2115)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

