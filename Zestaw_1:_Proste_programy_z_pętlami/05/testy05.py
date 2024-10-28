import unittest
import os
import sys
import importlib

from szablon05 import Zadanie_5


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

    def test_Nr01_Zadanie_5_argumenty_0(self):
        wynik = Zadanie_5(0)

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_Zadanie_5_argumenty_1(self):
        wynik = Zadanie_5(1)

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_Zadanie_5_argumenty_3(self):
        wynik = Zadanie_5(3)

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_Zadanie_5_argumenty_4(self):
        wynik = Zadanie_5(4)

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_Zadanie_5_argumenty_10(self):
        wynik = Zadanie_5(10)

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_Zadanie_5_argumenty_11(self):
        wynik = Zadanie_5(11)

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_Zadanie_5_argumenty_1(self):
        wynik = Zadanie_5(1)

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_Zadanie_5_argumenty_15(self):
        wynik = Zadanie_5(15)

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_Zadanie_5_argumenty_16(self):
        wynik = Zadanie_5(16)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_5_argumenty_20(self):
        wynik = Zadanie_5(20)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_5_argumenty_123(self):
        wynik = Zadanie_5(123)

        oczekiwany_wynik = 11
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr12_Zadanie_5_argumenty_1234(self):
        wynik = Zadanie_5(1234)

        oczekiwany_wynik = 35
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr13_Zadanie_5_argumenty_1410(self):
        wynik = Zadanie_5(1410)

        oczekiwany_wynik = 37
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr14_Zadanie_5_argumenty_1610(self):
        wynik = Zadanie_5(1610)

        oczekiwany_wynik = 40
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr15_Zadanie_5_argumenty_2000(self):
        wynik = Zadanie_5(2000)

        oczekiwany_wynik = 44
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr16_Zadanie_5_argumenty_3000(self):
        wynik = Zadanie_5(3000)

        oczekiwany_wynik = 54
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr17_Zadanie_5_argumenty_5000(self):
        wynik = Zadanie_5(5000)

        oczekiwany_wynik = 70
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr18_Zadanie_5_argumenty_100000(self):
        wynik = Zadanie_5(100000)

        oczekiwany_wynik = 316
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr19_Zadanie_5_argumenty_4473225(self):
        wynik = Zadanie_5(4473225)

        oczekiwany_wynik = 2115
        self.assertEqual(wynik, oczekiwany_wynik)
