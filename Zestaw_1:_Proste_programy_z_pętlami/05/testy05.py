import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon05 import Zadanie_5


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_Zadanie_5_argumenty_minus_1(self):
        wynik = Zadanie_5(1)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_Zadanie_5_argumenty_minus_5(self):
        wynik = Zadanie_5(5)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_Zadanie_5_argumenty_12(self):
        wynik = Zadanie_5(12)

        oczekiwany_wynik = [3]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_Zadanie_5_argumenty_213(self):
        wynik = Zadanie_5(213)

        oczekiwany_wynik = [14]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_Zadanie_5_argumenty_123(self):
        wynik = Zadanie_5(123)

        oczekiwany_wynik = [11]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_Zadanie_5_argumenty_123(self):
        wynik = Zadanie_5(123)

        oczekiwany_wynik = [11]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_Zadanie_5_argumenty_12(self):
        wynik = Zadanie_5(12)

        oczekiwany_wynik = [3]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_Zadanie_5_argumenty_312(self):
        wynik = Zadanie_5(312)

        oczekiwany_wynik = [17]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_Zadanie_5_argumenty_0(self):
        wynik = Zadanie_5(0)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_5_argumenty_2(self):
        wynik = Zadanie_5(2)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_5_argumenty_1(self):
        wynik = Zadanie_5(1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)
