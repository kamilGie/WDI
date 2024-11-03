import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon55 import Zadanie_55


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

    def test_Nr01_Zadanie_55_argumenty_123_522(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(123, 522)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '11')
    def test_Nr02_Zadanie_55_argumenty_57_48(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(57, 48)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '7')
    def test_Nr03_Zadanie_55_argumenty_987654321_123456789(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(987654321, 123456789)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, 'brak')
    def test_Nr04_Zadanie_55_argumenty_7_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(7, 4)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '5')
    def test_Nr05_Zadanie_55_argumenty_22_22(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(22, 22)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, 'brak')
    def test_Nr06_Zadanie_55_argumenty_0_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(0, 1)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '2')
    def test_Nr07_Zadanie_55_argumenty_555_444(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(555, 444)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '8')
    def test_Nr08_Zadanie_55_argumenty_123456_7890(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(123456, 7890)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '10')
    def test_Nr09_Zadanie_55_argumenty_123_789(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(123, 789)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '10')
    def test_Nr10_Zadanie_55_argumenty_0_1234(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(0, 1234)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '2')
    def test_Nr11_Zadanie_55_argumenty_2115_1410(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_55(2115, 1410)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '7')

