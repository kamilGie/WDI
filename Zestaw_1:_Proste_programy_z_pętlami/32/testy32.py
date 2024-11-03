import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon32 import Zadanie_32


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

    def test_Nr01_Zadanie_32_argumenty_1(self):
        wynik  = Zadanie_32(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_Zadanie_32_argumenty_123(self):
        wynik  = Zadanie_32(123)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_Zadanie_32_argumenty_123456789(self):
        wynik  = Zadanie_32(123456789)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_Zadanie_32_argumenty_321(self):
        wynik  = Zadanie_32(321)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_Zadanie_32_argumenty_9876543210(self):
        wynik  = Zadanie_32(9876543210)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_Zadanie_32_argumenty_123454(self):
        wynik  = Zadanie_32(123454)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_Zadanie_32_argumenty_1230(self):
        wynik  = Zadanie_32(1230)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_Zadanie_32_argumenty_1232(self):
        wynik  = Zadanie_32(1232)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_Zadanie_32_argumenty_1223(self):
        wynik  = Zadanie_32(1223)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_32_argumenty_111(self):
        wynik  = Zadanie_32(111)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_32_argumenty_0(self):
        wynik  = Zadanie_32(0)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_Zadanie_32_argumenty_1234567889(self):
        wynik  = Zadanie_32(1234567889)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_Zadanie_32_argumenty_1234567899(self):
        wynik  = Zadanie_32(1234567899)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_Zadanie_32_argumenty_12343456789(self):
        wynik  = Zadanie_32(12343456789)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr15_Zadanie_32_argumenty_2115(self):
        wynik  = Zadanie_32(2115)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

