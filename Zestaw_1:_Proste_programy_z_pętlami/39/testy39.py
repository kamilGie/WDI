import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon39 import Zadanie_39


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

    def test_Nr01_Zadanie_39_argumenty_1(self):
        wynik  = Zadanie_39(1)

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_Zadanie_39_argumenty_5(self):
        wynik  = Zadanie_39(5)

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_Zadanie_39_argumenty_10(self):
        wynik  = Zadanie_39(10)

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_Zadanie_39_argumenty_20(self):
        wynik  = Zadanie_39(20)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_Zadanie_39_argumenty_25(self):
        wynik  = Zadanie_39(25)

        oczekiwany_wynik = 6
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_Zadanie_39_argumenty_50(self):
        wynik  = Zadanie_39(50)

        oczekiwany_wynik = 12
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_Zadanie_39_argumenty_100(self):
        wynik  = Zadanie_39(100)

        oczekiwany_wynik = 24
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_Zadanie_39_argumenty_1000(self):
        wynik  = Zadanie_39(1000)

        oczekiwany_wynik = 249
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_Zadanie_39_argumenty_2000(self):
        wynik  = Zadanie_39(2000)

        oczekiwany_wynik = 499
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_39_argumenty_5000(self):
        wynik  = Zadanie_39(5000)

        oczekiwany_wynik = 1249
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_39_argumenty_10001(self):
        wynik  = Zadanie_39(10001)

        oczekiwany_wynik = 2499
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_Zadanie_39_argumenty_10099(self):
        wynik  = Zadanie_39(10099)

        oczekiwany_wynik = 2521
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_Zadanie_39_argumenty_10100(self):
        wynik  = Zadanie_39(10100)

        oczekiwany_wynik = 2523
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_Zadanie_39_argumenty_2115(self):
        wynik  = Zadanie_39(2115)

        oczekiwany_wynik = 526
        self.assertEqual(wynik, oczekiwany_wynik)

