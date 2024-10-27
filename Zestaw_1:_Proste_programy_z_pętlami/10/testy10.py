import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon10 import Zadanie_10


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2).run(suite)


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
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_Zadanie_10_argumenty_13(self):
        wynik  = Zadanie_10(13)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr2_Zadanie_10_argumenty_2(self):
        wynik  = Zadanie_10(2)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr3_Zadanie_10_argumenty_1(self):
        wynik  = Zadanie_10(1)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr4_Zadanie_10_argumenty_73(self):
        wynik  = Zadanie_10(73)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr5_Zadanie_10_argumenty_317(self):
        wynik  = Zadanie_10(317)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr6_Zadanie_10_argumenty_129(self):
        wynik  = Zadanie_10(129)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr7_Zadanie_10_argumenty_577(self):
        wynik  = Zadanie_10(577)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr8_Zadanie_10_argumenty_279(self):
        wynik  = Zadanie_10(279)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr9_Zadanie_10_argumenty_157(self):
        wynik  = Zadanie_10(157)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_10_argumenty_779(self):
        wynik  = Zadanie_10(779)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_10_argumenty_minus_6_0f(self):
        wynik  = Zadanie_10(-6.0)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

