import unittest
import os
import sys
import importlib

from szablon04 import is_in_fib


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

    def test_Nr1_is_in_fib_argumenty_1(self):
        wynik = is_in_fib(1)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_is_in_fib_argumenty_2(self):
        wynik = is_in_fib(2)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_is_in_fib_argumenty_4(self):
        wynik = is_in_fib(4)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_is_in_fib_argumenty_0(self):
        wynik = is_in_fib(0)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_is_in_fib_argumenty_100(self):
        wynik = is_in_fib(100)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_is_in_fib_argumenty_1000(self):
        wynik = is_in_fib(1000)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_is_in_fib_argumenty_10(self):
        wynik = is_in_fib(10)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_is_in_fib_argumenty_14(self):
        wynik = is_in_fib(14)

        oczekiwany_wynik = [False]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_is_in_fib_argumenty_143(self):
        wynik = is_in_fib(143)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_is_in_fib_argumenty_376(self):
        wynik = is_in_fib(376)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_is_in_fib_argumenty_1597(self):
        wynik = is_in_fib(1597)

        oczekiwany_wynik = [True]
        self.assertIn(wynik, oczekiwany_wynik)
