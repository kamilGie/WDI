import unittest
import os
import sys
import importlib

from szablon25 import Zadanie_25


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

    def test_Nr01_Zadanie_25_argumenty_1(self):
        wynik = Zadanie_25(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_Zadanie_25_argumenty_2(self):
        wynik = Zadanie_25(2)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_Zadanie_25_argumenty_5(self):
        wynik = Zadanie_25(5)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_Zadanie_25_argumenty_21(self):
        wynik = Zadanie_25(21)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_Zadanie_25_argumenty_55(self):
        wynik = Zadanie_25(55)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_Zadanie_25_argumenty_10(self):
        wynik = Zadanie_25(10)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_Zadanie_25_argumenty_50(self):
        wynik = Zadanie_25(50)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_Zadanie_25_argumenty_7(self):
        wynik = Zadanie_25(7)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_Zadanie_25_argumenty_0(self):
        wynik = Zadanie_25(0)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_25_argumenty_17(self):
        wynik = Zadanie_25(17)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_25_argumenty_29(self):
        wynik = Zadanie_25(29)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr12_Zadanie_25_argumenty_64(self):
        wynik = Zadanie_25(64)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr13_Zadanie_25_argumenty_832040(self):
        wynik = Zadanie_25(832040)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr14_Zadanie_25_argumenty_5702887(self):
        wynik = Zadanie_25(5702887)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr15_Zadanie_25_argumenty_427859097160(self):
        wynik = Zadanie_25(427859097160)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr16_Zadanie_25_argumenty_2115(self):
        wynik = Zadanie_25(2115)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
