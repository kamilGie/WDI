import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon29 import czy_ciag


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

    def test_Nr01_czy_ciag_argumenty_1(self):
        wynik  = czy_ciag(1)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_czy_ciag_argumenty_3(self):
        wynik  = czy_ciag(3)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_czy_ciag_argumenty_6(self):
        wynik  = czy_ciag(6)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_czy_ciag_argumenty_7(self):
        wynik  = czy_ciag(7)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_czy_ciag_argumenty_10(self):
        wynik  = czy_ciag(10)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_czy_ciag_argumenty_12(self):
        wynik  = czy_ciag(12)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_czy_ciag_argumenty_15(self):
        wynik  = czy_ciag(15)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_czy_ciag_argumenty_123(self):
        wynik  = czy_ciag(123)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_czy_ciag_argumenty_63(self):
        wynik  = czy_ciag(63)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_czy_ciag_argumenty_29(self):
        wynik  = czy_ciag(29)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_czy_ciag_argumenty_303(self):
        wynik  = czy_ciag(303)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_czy_ciag_argumenty_3003(self):
        wynik  = czy_ciag(3003)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_czy_ciag_argumenty_100000(self):
        wynik  = czy_ciag(100000)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_czy_ciag_argumenty_1001(self):
        wynik  = czy_ciag(1001)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr15_czy_ciag_argumenty_14641(self):
        wynik  = czy_ciag(14641)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr16_czy_ciag_argumenty_2115(self):
        wynik  = czy_ciag(2115)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

