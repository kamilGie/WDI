import unittest
import os
import sys
import importlib

from szablon77 import Zadanie_77


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

    def test_Nr01_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([1, 3, 5, 3, 1])

        oczekiwany_wynik = 5
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([2, 1, 3, 5, 3, 1, 6, 4])

        oczekiwany_wynik = 5
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([2, 4, 6, 8, 10])

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([2, 4, 6, 1, 8, 10])

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([1, 1, 1, 1, 1])

        oczekiwany_wynik = 5
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([1, 3, 5, 7, 3, 1, 5, 3, 1])

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([2, 2, 1, 4, 4])

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([])

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([1, 2, 3, 4, 5, 6, 7])

        oczekiwany_wynik = 0
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_77_argumenty_tablica(self):
        wynik = Zadanie_77([2, 7, 5, 3, 5, 7, 2])

        oczekiwany_wynik = 5
        self.assertEqual(wynik, oczekiwany_wynik)
