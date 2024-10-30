import unittest
import os
import sys
import importlib

from szablon68 import Zadanie_68


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

    def test_Nr01_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([1, 2, 3, 4, 5, 6])

        oczekiwany_wynik = 6
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr02_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([6, 5, 4, 3, 2, 1])

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr03_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([1, 2, 2, 3, 4, 4, 5, 6])

        oczekiwany_wynik = 3
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr04_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([1, 3, 1, 3, 1, 3, 1, 3])

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr05_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([7, 1, 2, 3, 4, 5, 2, 1])

        oczekiwany_wynik = 5
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr06_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([1])

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr07_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([1, 3, 2, 4, 3, 5, 4, 6])

        oczekiwany_wynik = 2
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr08_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([5, 3, 1, 2, 3, 4, 5, 6])

        oczekiwany_wynik = 6
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_Nr09_Zadanie_68_argumenty_tablica(self):
        wynik = Zadanie_68([7, 7, 7, 7, 7])

        oczekiwany_wynik = 1
        self.assertEqual(wynik, oczekiwany_wynik)


if __name__ == "__main__":
    unittest.main()
