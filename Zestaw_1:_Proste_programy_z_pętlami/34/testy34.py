import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon34 import Zadanie_34


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

    def test_Nr01_Zadanie_34_argumenty_1(self):
        wynik  = Zadanie_34(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_Zadanie_34_argumenty_2(self):
        wynik  = Zadanie_34(2)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_Zadanie_34_argumenty_11(self):
        wynik  = Zadanie_34(11)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_Zadanie_34_argumenty_22(self):
        wynik  = Zadanie_34(22)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_Zadanie_34_argumenty_321(self):
        wynik  = Zadanie_34(321)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_Zadanie_34_argumenty_400(self):
        wynik  = Zadanie_34(400)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_Zadanie_34_argumenty_4321(self):
        wynik  = Zadanie_34(4321)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_Zadanie_34_argumenty_987654321(self):
        wynik  = Zadanie_34(987654321)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_Zadanie_34_argumenty_807654321(self):
        wynik  = Zadanie_34(807654321)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_Zadanie_34_argumenty_9876543210(self):
        wynik  = Zadanie_34(9876543210)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_Zadanie_34_argumenty_2115(self):
        wynik  = Zadanie_34(2115)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

