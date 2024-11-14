import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon125 import dodawanie, odejmowanie, mnozenie, dzielenie, potegowanie, wypisywanie


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_dodawanie_argumenty_tablica_tablica(self):
            self.assertEqual(dodawanie([3, 4], [1, 2]), (4, 4))

    def test_Nr02_dodawanie_argumenty_tablica_tablica(self):
            self.assertEqual(dodawanie([5, -3], [2, 6]), (7, 12))

    def test_Nr03_dodawanie_argumenty_tablica_tablica(self):
            self.assertEqual(dodawanie([0, 0], [0, 0]), (0, 0))

    def test_Nr04_dodawanie_argumenty_tablica_tablica(self):
            self.assertEqual(dodawanie([-1, 2], [3, -4]), (2, -8))

    def test_Nr01_odejmowanie_argumenty_tablica_tablica(self):
            self.assertEqual(odejmowanie([3, 4], [1, 2]), (2, 0))

    def test_Nr02_odejmowanie_argumenty_tablica_tablica(self):
            self.assertEqual(odejmowanie([5, -3], [2, 6]), (3, 0))

    def test_Nr03_odejmowanie_argumenty_tablica_tablica(self):
            self.assertEqual(odejmowanie([0, 0], [0, 0]), (0, 0))

    def test_Nr04_odejmowanie_argumenty_tablica_tablica(self):
            self.assertEqual(odejmowanie([-1, 2], [3, -4]), (-4, 0))

    def test_Nr01_mnozenie_argumenty_tablica_tablica(self):
            self.assertEqual(mnozenie([3, 4], [1, 2]), (-5, 10))

    def test_Nr02_mnozenie_argumenty_tablica_tablica(self):
            self.assertEqual(mnozenie([1, -1], [2, 3]), (5, 1))

    def test_Nr03_mnozenie_argumenty_tablica_tablica(self):
            self.assertEqual(mnozenie([0, 0], [1, 1]), (0, 0))

    def test_Nr04_mnozenie_argumenty_tablica_tablica(self):
            self.assertEqual(mnozenie([-1, 2], [3, -4]), (5, 10))

    def test_Nr05_mnozenie_argumenty_tablica_tablica(self):
            self.assertEqual(mnozenie([3, 4], [1, 2]), (-5, 10))

    def test_Nr01_dzielenie_argumenty_tablica_tablica(self):
            self.assertEqual(dzielenie([3, 4], [1, 2]), (-1.6666666666666667, 3.3333333333333335))

    def test_Nr02_dzielenie_argumenty_tablica_tablica(self):
            self.assertEqual(dzielenie([1, -1], [2, 3]), (1.0, 0.2))

    def test_Nr03_dzielenie_argumenty_tablica_tablica(self):
            self.assertEqual(dzielenie([0, 0], [1, 1]), (0.0, 0.0))

    def test_Nr04_dzielenie_argumenty_tablica_tablica(self):
            self.assertEqual(dzielenie([-1, 2], [3, -4]), (-5.0, -10.0))

    def test_Nr01_potegowanie_argumenty_tablica_2(self):
            self.assertEqual(potegowanie([1, 1], 2), 2j)

    def test_Nr02_potegowanie_argumenty_tablica_2(self):
            self.assertEqual(potegowanie([2, 3], 2), (-5+12j))

    def test_Nr03_potegowanie_argumenty_tablica_3(self):
            self.assertEqual(potegowanie([0, 0], 3), 0j)

    def test_Nr04_potegowanie_argumenty_tablica_3(self):
            self.assertEqual(potegowanie([-1, -1], 3), (2-2j))

    def test_Nr01_wypisywanie_argumenty_tablica(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wypisywanie([3, 4])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '3 + 4i')

    def test_Nr02_wypisywanie_argumenty_tablica(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wypisywanie([5, -3])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '5 + -3i')

    def test_Nr03_wypisywanie_argumenty_tablica(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wypisywanie([0, 0])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '0 + 0i')

    def test_Nr04_wypisywanie_argumenty_tablica(self):
            f = io.StringIO()
            with redirect_stdout(f):
                wypisywanie([-1, 2])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '-1 + 2i')


