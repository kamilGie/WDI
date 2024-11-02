import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon23 import average


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

    def test_Nr01_average_argumenty_1_1(self):
        wynik = average(1, 1)

        oczekiwany_wynik = 1.0
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr02_average_argumenty_3_4(self):
        wynik = average(3, 4)

        oczekiwany_wynik = 3.4820276763595706
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr03_average_argumenty_12_1(self):
        wynik = average(12, 1)

        oczekiwany_wynik = 4.862890376598251
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr04_average_argumenty_9_12(self):
        wynik = average(9, 12)

        oczekiwany_wynik = 10.44608302907871
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr05_average_argumenty_1_1(self):
        wynik = average(1, 1)

        oczekiwany_wynik = 1.0
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr06_average_argumenty_32_52(self):
        wynik = average(32, 52)

        oczekiwany_wynik = 41.39387527336875
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr07_average_argumenty_1_12345(self):
        wynik = average(1, 12345)

        oczekiwany_wynik = 1794.2945283789873
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr08_average_argumenty_21_23(self):
        wynik = average(21, 23)

        oczekiwany_wynik = 21.9886290182287
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr09_average_argumenty_19_10(self):
        wynik = average(19, 10)

        oczekiwany_wynik = 14.139758572153811
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr10_average_argumenty_1_0(self):
        wynik = average(1, 0)

        oczekiwany_wynik = 4.76837158203125e-07
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr11_average_argumenty_0_0(self):
        wynik = average(0, 0)

        oczekiwany_wynik = 0.0
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr12_average_argumenty_1_2115(self):
        wynik = average(1, 2115)

        oczekiwany_wynik = 367.3776061576534
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr13_average_argumenty_1410_2004(self):
        wynik = average(1410, 2004)

        oczekiwany_wynik = 1693.956993773465
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr14_average_argumenty_2115_1337(self):
        wynik = average(2115, 1337)

        oczekiwany_wynik = 1703.7241557414884
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)
