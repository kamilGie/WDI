import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon35 import Zadanie_35


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

    def test_Nr01_Zadanie_35_argumenty_1(self):
        wynik  = Zadanie_35(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_Zadanie_35_argumenty_5(self):
        wynik  = Zadanie_35(5)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_Zadanie_35_argumenty_9(self):
        wynik  = Zadanie_35(9)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_Zadanie_35_argumenty_10(self):
        wynik  = Zadanie_35(10)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_Zadanie_35_argumenty_123(self):
        wynik  = Zadanie_35(123)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_Zadanie_35_argumenty_121(self):
        wynik  = Zadanie_35(121)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_Zadanie_35_argumenty_12345678904(self):
        wynik  = Zadanie_35(12345678904)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_Zadanie_35_argumenty_9123124(self):
        wynik  = Zadanie_35(9123124)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_Zadanie_35_argumenty_12983125126(self):
        wynik  = Zadanie_35(12983125126)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_35_argumenty_102380214(self):
        wynik  = Zadanie_35(102380214)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_35_argumenty_91271(self):
        wynik  = Zadanie_35(91271)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_Zadanie_35_argumenty_91111111111119(self):
        wynik  = Zadanie_35(91111111111119)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_Zadanie_35_argumenty_2115(self):
        wynik  = Zadanie_35(2115)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

