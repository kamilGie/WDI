import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon16 import NWW_3


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

    def test_Nr01_NWW_3_argumenty_1_1_1(self):
        wynik  = NWW_3(1, 1, 1)

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_NWW_3_argumenty_21_21_21(self):
        wynik  = NWW_3(21, 21, 21)

        oczekiwany_wynik = 21
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_NWW_3_argumenty_100_10_5(self):
        wynik  = NWW_3(100, 10, 5)

        oczekiwany_wynik = 100
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_NWW_3_argumenty_4_5_6(self):
        wynik  = NWW_3(4, 5, 6)

        oczekiwany_wynik = 60
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_NWW_3_argumenty_3_5_7(self):
        wynik  = NWW_3(3, 5, 7)

        oczekiwany_wynik = 105
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_NWW_3_argumenty_12_15_20(self):
        wynik  = NWW_3(12, 15, 20)

        oczekiwany_wynik = 60
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_NWW_3_argumenty_100000_250000_300000(self):
        wynik  = NWW_3(100000, 250000, 300000)

        oczekiwany_wynik = 1500000
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_NWW_3_argumenty_2_3_4(self):
        wynik  = NWW_3(2, 3, 4)

        oczekiwany_wynik = 12
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_NWW_3_argumenty_1_1000000_10000000(self):
        wynik  = NWW_3(1, 1000000, 10000000)

        oczekiwany_wynik = 10000000
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_NWW_3_argumenty_123_41_21(self):
        wynik  = NWW_3(123, 41, 21)

        oczekiwany_wynik = 861
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_NWW_3_argumenty_123_41_2(self):
        wynik  = NWW_3(123, 41, 2)

        oczekiwany_wynik = 246
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_NWW_3_argumenty_98_123_5213(self):
        wynik  = NWW_3(98, 123, 5213)

        oczekiwany_wynik = 62837502
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_NWW_3_argumenty_2115_1410_2004(self):
        wynik  = NWW_3(2115, 1410, 2004)

        oczekiwany_wynik = 1412820
        self.assertEqual(wynik, oczekiwany_wynik)

