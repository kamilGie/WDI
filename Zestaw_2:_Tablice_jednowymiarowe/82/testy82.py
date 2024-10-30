import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon82 import n_liczba_z_pierwiastka_z_2


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

    def test_Nr01_n_liczba_z_pierwiastka_z_2_argumenty_1(self):
        wynik = n_liczba_z_pierwiastka_z_2(1)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_n_liczba_z_pierwiastka_z_2_argumenty_4(self):
        wynik = n_liczba_z_pierwiastka_z_2(4)

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_n_liczba_z_pierwiastka_z_2_argumenty_10(self):
        wynik = n_liczba_z_pierwiastka_z_2(10)

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_n_liczba_z_pierwiastka_z_2_argumenty_12(self):
        wynik = n_liczba_z_pierwiastka_z_2(12)

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_n_liczba_z_pierwiastka_z_2_argumenty_19(self):
        wynik = n_liczba_z_pierwiastka_z_2(19)

        oczekiwany_wynik = 8
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_n_liczba_z_pierwiastka_z_2_argumenty_20(self):
        wynik = n_liczba_z_pierwiastka_z_2(20)

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_n_liczba_z_pierwiastka_z_2_argumenty_30(self):
        wynik = n_liczba_z_pierwiastka_z_2(30)

        oczekiwany_wynik = 9
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_n_liczba_z_pierwiastka_z_2_argumenty_40(self):
        wynik = n_liczba_z_pierwiastka_z_2(40)

        oczekiwany_wynik = 6
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_n_liczba_z_pierwiastka_z_2_argumenty_50(self):
        wynik = n_liczba_z_pierwiastka_z_2(50)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_n_liczba_z_pierwiastka_z_2_argumenty_60(self):
        wynik = n_liczba_z_pierwiastka_z_2(60)

        oczekiwany_wynik = 9
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr11_n_liczba_z_pierwiastka_z_2_argumenty_70(self):
        wynik = n_liczba_z_pierwiastka_z_2(70)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr12_n_liczba_z_pierwiastka_z_2_argumenty_80(self):
        wynik = n_liczba_z_pierwiastka_z_2(80)

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr13_n_liczba_z_pierwiastka_z_2_argumenty_88(self):
        wynik = n_liczba_z_pierwiastka_z_2(88)

        oczekiwany_wynik = 5
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr14_n_liczba_z_pierwiastka_z_2_argumenty_90(self):
        wynik = n_liczba_z_pierwiastka_z_2(90)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr15_n_liczba_z_pierwiastka_z_2_argumenty_92(self):
        wynik = n_liczba_z_pierwiastka_z_2(92)

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr16_n_liczba_z_pierwiastka_z_2_argumenty_95(self):
        wynik = n_liczba_z_pierwiastka_z_2(95)

        oczekiwany_wynik = 4
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr17_n_liczba_z_pierwiastka_z_2_argumenty_99(self):
        wynik = n_liczba_z_pierwiastka_z_2(99)

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)
