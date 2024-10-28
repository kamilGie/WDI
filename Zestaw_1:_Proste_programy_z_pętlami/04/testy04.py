import unittest
import os
import sys
import importlib

from szablon04 import is_in_fib


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

    def test_Nr01_is_in_fib_argumenty_0(self):
        wynik = is_in_fib(0)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_is_in_fib_argumenty_1(self):
        wynik = is_in_fib(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_is_in_fib_argumenty_4(self):
        wynik = is_in_fib(4)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_is_in_fib_argumenty_10(self):
        wynik = is_in_fib(10)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_is_in_fib_argumenty_8(self):
        wynik = is_in_fib(8)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_is_in_fib_argumenty_24(self):
        wynik = is_in_fib(24)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_is_in_fib_argumenty_30(self):
        wynik = is_in_fib(30)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_is_in_fib_argumenty_81(self):
        wynik = is_in_fib(81)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_is_in_fib_argumenty_123(self):
        wynik = is_in_fib(123)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_is_in_fib_argumenty_341(self):
        wynik = is_in_fib(341)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr11_is_in_fib_argumenty_613(self):
        wynik = is_in_fib(613)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr12_is_in_fib_argumenty_1597(self):
        wynik = is_in_fib(1597)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr13_is_in_fib_argumenty_610(self):
        wynik = is_in_fib(610)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr14_is_in_fib_argumenty_2000(self):
        wynik = is_in_fib(2000)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr15_is_in_fib_argumenty_2004(self):
        wynik = is_in_fib(2004)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr16_is_in_fib_argumenty_2115(self):
        wynik = is_in_fib(2115)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
