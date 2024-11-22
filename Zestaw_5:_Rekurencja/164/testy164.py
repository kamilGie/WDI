import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon164 import Zadanie_164


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

    def test_Nr01_Zadanie_164_argumenty_60(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(60)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3, 5] 71")

    def test_Nr02_Zadanie_164_argumenty_50(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(50)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 5] 17")

    def test_Nr03_Zadanie_164_argumenty_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(20)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 5] 17")

    def test_Nr04_Zadanie_164_argumenty_72(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(72)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 3] 11")

    def test_Nr05_Zadanie_164_argumenty_98(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(98)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 7] 23")

    def test_Nr06_Zadanie_164_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(100)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[2, 5] 17")

    def test_Nr07_Zadanie_164_argumenty_123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(123)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[3, 41] 167")

    def test_Nr08_Zadanie_164_argumenty_541(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(541)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[541] 541")

    def test_Nr10_Zadanie_164_argumenty_5123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(5123)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[47, 109] 5279")

    def test_Nr11_Zadanie_164_argumenty_71293(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(71293)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[71293] 71293")

    def test_Nr12_Zadanie_164_argumenty_123123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(123123)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[3, 7, 11, 13, 41] 225791")

    def test_Nr13_Zadanie_164_argumenty_2135(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(2135)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[5, 7, 61] 2975")

    def test_Nr14_Zadanie_164_argumenty_123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(123)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[3, 41] 167")

    def test_Nr15_Zadanie_164_argumenty_521(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(521)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[521] 521")

    def test_Nr16_Zadanie_164_argumenty_581(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_164(581)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "[7, 83] 671")
