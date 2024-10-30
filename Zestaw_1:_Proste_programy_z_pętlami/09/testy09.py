import unittest
import os
import sys
import importlib

from szablon09 import iloczyn


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


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
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_iloczyn_argumenty_2(self):
        wynik = iloczyn(2)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_iloczyn_argumenty_6(self):
        wynik = iloczyn(6)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_iloczyn_argumenty_104(self):
        wynik = iloczyn(104)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_iloczyn_argumenty_714(self):
        wynik = iloczyn(714)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_iloczyn_argumenty_1(self):
        wynik = iloczyn(1)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_iloczyn_argumenty_0(self):
        wynik = iloczyn(0)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_iloczyn_argumenty_200(self):
        wynik = iloczyn(200)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_iloczyn_argumenty_701408733(self):
        wynik = iloczyn(701408733)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_iloczyn_argumenty_317811(self):
        wynik = iloczyn(317811)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_iloczyn_argumenty_10946(self):
        wynik = iloczyn(10946)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_iloczyn_argumenty_1576239(self):
        wynik = iloczyn(1576239)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
