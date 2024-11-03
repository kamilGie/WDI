import unittest
import os
import sys
import importlib

from szablon40 import Zadanie_40


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

    def test_Nr01_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+b")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+b*c")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("(a+b)")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+(b+c)")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+b)")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("+a+b+c")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("(((a+b)))")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+b*(a*c)")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+b+(c*b)+a)")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a(+b)")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a**b")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr12_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("aa+b")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr13_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("(a+b+(c+a(a+b)))")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr14_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40(")a+b(")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr15_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("(a+b)*c)")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr16_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+(b*(a+b)*c)")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr17_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+(a*b+a*(a+b)))+c*a(b+a")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr18_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("(a+b*(c+a)")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr19_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("+a-b")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr20_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a+b*")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr21_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a*b*c*d*a*d*a*b*a*(a+b+c+d+e+d+f+g+a+((a*(a+b))))")

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr22_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a(b)c")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr23_Zadanie_40_argumenty_(self):
        wynik = Zadanie_40("a*(bc)")

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
