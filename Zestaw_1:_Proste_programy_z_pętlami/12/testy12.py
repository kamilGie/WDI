import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon12 import Czynniki


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

    def test_Nr1_Czynniki_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(1)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == set())  # Porównanie z użyciem set

    def test_Nr2_Czynniki_argumenty_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(2)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"2"})  # Porównanie z użyciem set

    def test_Nr3_Czynniki_argumenty_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(4)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"2"})  # Porównanie z użyciem set

    def test_Nr4_Czynniki_argumenty_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(8)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"2"})  # Porównanie z użyciem set

    def test_Nr5_Czynniki_argumenty_36(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(36)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"3", "2"})  # Porównanie z użyciem set

    def test_Nr6_Czynniki_argumenty_360(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(360)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"5", "3", "2"}
        )  # Porównanie z użyciem set

    def test_Nr7_Czynniki_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(100)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"5", "2"})  # Porównanie z użyciem set

    def test_Nr8_Czynniki_argumenty_1000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(1000)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"5", "2"})  # Porównanie z użyciem set

    def test_Nr9_Czynniki_argumenty_12312(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(12312)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"3", "19", "2"}
        )  # Porównanie z użyciem set

    def test_Nr10_Czynniki_argumenty_89342342(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(89342342)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"2", "44671171"}
        )  # Porównanie z użyciem set

    def test_Nr11_Czynniki_argumenty_4987239(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(4987239)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"3", "17", "97789"}
        )  # Porównanie z użyciem set

    def test_Nr12_Czynniki_argumenty_789273948(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(789273948)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"3", "1097", "2", "59957"}
        )  # Porównanie z użyciem set

    def test_Nr13_Czynniki_argumenty_104729(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(104729)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"104729"})  # Porównanie z użyciem set

    def test_Nr14_Czynniki_argumenty_102191(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(102191)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"102191"})  # Porównanie z użyciem set

    def test_Nr15_Czynniki_argumenty_23456789(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(23456789)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"23456789"})  # Porównanie z użyciem set

    def test_Nr16_Czynniki_argumenty_1024(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(1024)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {"2"})  # Porównanie z użyciem set

    def test_Nr17_Czynniki_argumenty_1410(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(1410)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"5", "3", "2", "47"}
        )  # Porównanie z użyciem set

    def test_Nr18_Czynniki_argumenty_204382(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(204382)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"102191", "2"}
        )  # Porównanie z użyciem set

    def test_Nr19_Czynniki_argumenty_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(0)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == set())  # Porównanie z użyciem set

    def test_Nr20_Czynniki_argumenty_20342342(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(20342342)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"2", "79", "128749"}
        )  # Porównanie z użyciem set

    def test_Nr21_Czynniki_argumenty_2115(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Czynniki(2115)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(
            set(wynik.split()) == {"3", "5", "47"}
        )  # Porównanie z użyciem set
