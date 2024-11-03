import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon28 import Zadanie_28


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

    def test_Nr01_Zadanie_28_argumenty_1(self):
        wynik  = Zadanie_28(1)

        oczekiwany_wynik = (1, 1)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_Zadanie_28_argumenty_4(self):
        wynik  = Zadanie_28(4)

        oczekiwany_wynik = (2, 2)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_Zadanie_28_argumenty_5(self):
        wynik  = Zadanie_28(5)

        oczekiwany_wynik = (1, 5)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_Zadanie_28_argumenty_6(self):
        wynik  = Zadanie_28(6)

        oczekiwany_wynik = (2, 3)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_Zadanie_28_argumenty_10(self):
        wynik  = Zadanie_28(10)

        oczekiwany_wynik = (2, 5)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_Zadanie_28_argumenty_12(self):
        wynik  = Zadanie_28(12)

        oczekiwany_wynik = (3, 4)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_Zadanie_28_argumenty_30(self):
        wynik  = Zadanie_28(30)

        oczekiwany_wynik = (5, 6)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_Zadanie_28_argumenty_120(self):
        wynik  = Zadanie_28(120)

        oczekiwany_wynik = (10, 12)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_Zadanie_28_argumenty_200(self):
        wynik  = Zadanie_28(200)

        oczekiwany_wynik = (10, 20)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_28_argumenty_123(self):
        wynik  = Zadanie_28(123)

        oczekiwany_wynik = (3, 41)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_28_argumenty_2004(self):
        wynik  = Zadanie_28(2004)

        oczekiwany_wynik = (12, 167)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_Zadanie_28_argumenty_2500(self):
        wynik  = Zadanie_28(2500)

        oczekiwany_wynik = (50, 50)
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_Zadanie_28_argumenty_2115(self):
        wynik  = Zadanie_28(2115)

        oczekiwany_wynik = (45, 47)
        self.assertEqual(wynik, oczekiwany_wynik)

