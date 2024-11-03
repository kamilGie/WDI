import unittest
import os
import sys
import importlib

from szablon21 import golden_ratio


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

    def test_Nr01_golden_ratio_argumenty_1_1(self):
        wynik = golden_ratio(1, 1)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr02_golden_ratio_argumenty_2_2(self):
        wynik = golden_ratio(2, 2)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr03_golden_ratio_argumenty_3_3(self):
        wynik = golden_ratio(3, 3)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr04_golden_ratio_argumenty_123_123(self):
        wynik = golden_ratio(123, 123)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr05_golden_ratio_argumenty_1_100(self):
        wynik = golden_ratio(1, 100)

        oczekiwany_wynik = 1.6180370653520681
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr06_golden_ratio_argumenty_2115_1(self):
        wynik = golden_ratio(2115, 1)

        oczekiwany_wynik = 1.6180371319544091
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr07_golden_ratio_argumenty_123_1(self):
        wynik = golden_ratio(123, 1)

        oczekiwany_wynik = 1.618037078819097
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr08_golden_ratio_argumenty_999_999(self):
        wynik = golden_ratio(999, 999)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr09_golden_ratio_argumenty_1_1(self):
        wynik = golden_ratio(1, 1)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr10_golden_ratio_argumenty_23_23(self):
        wynik = golden_ratio(23, 23)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr11_golden_ratio_argumenty_23_123(self):
        wynik = golden_ratio(23, 123)

        oczekiwany_wynik = 1.618028838635013
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr12_golden_ratio_argumenty_12_3(self):
        wynik = golden_ratio(12, 3)

        oczekiwany_wynik = 1.6180290297937356
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr13_golden_ratio_argumenty_1_1(self):
        wynik = golden_ratio(1, 1)

        oczekiwany_wynik = 1.6180371352785146
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)
