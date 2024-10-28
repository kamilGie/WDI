import unittest
import os
import sys
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

    def test_Nr1_Zadanie_5_argumenty_0(self):
        wynik = Zadanie_5(0)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_Zadanie_5_argumenty_1(self):
        wynik = Zadanie_5(1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_Zadanie_5_argumenty_3(self):
        wynik = Zadanie_5(3)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_Zadanie_5_argumenty_4(self):
        wynik = Zadanie_5(4)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_Zadanie_5_argumenty_8(self):
        wynik = Zadanie_5(8)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_Zadanie_5_argumenty_9(self):
        wynik = Zadanie_5(9)

        oczekiwany_wynik = [3]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_Zadanie_5_argumenty_12345(self):
        wynik = Zadanie_5(12345)

        oczekiwany_wynik = [111]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_Zadanie_5_argumenty_4473225(self):
        wynik = Zadanie_5(4473225)

        oczekiwany_wynik = [2115]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_Zadanie_5_argumenty_4473224(self):
        wynik = Zadanie_5(4473224)

        oczekiwany_wynik = [2114]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_5_argumenty_3000(self):
        wynik = Zadanie_5(3000)

        oczekiwany_wynik = [54]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_5_argumenty_17(self):
        wynik = Zadanie_5(17)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)
