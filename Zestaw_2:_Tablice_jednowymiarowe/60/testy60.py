import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon60 import Zadanie_60


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

    def test_Nr01_Zadanie_60_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(1)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1')
    def test_Nr02_Zadanie_60_argumenty_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(5)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '101 12 11 10 5 5 5 5 5 5 5 5 5 5 5')
    def test_Nr03_Zadanie_60_argumenty_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(10)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '1010 101 22 20 14 13 12 11 10 A A A A A A')
    def test_Nr04_Zadanie_60_argumenty_15(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(15)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '1111 120 33 30 23 21 17 16 15 14 13 12 11 10 F')
    def test_Nr05_Zadanie_60_argumenty_16(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(16)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '10000 121 100 31 24 22 20 17 16 15 14 13 12 11 10')
    def test_Nr06_Zadanie_60_argumenty_17(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(17)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '10001 122 101 32 25 23 21 18 17 16 15 14 13 12 11')
    def test_Nr07_Zadanie_60_argumenty_25(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(25)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '11001 221 121 100 41 34 31 27 25 23 21 1C 1B 1A 19')
    def test_Nr08_Zadanie_60_argumenty_54(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(54)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '110110 2000 312 204 130 105 66 60 54 4A 46 42 3C 39 36')
    def test_Nr09_Zadanie_60_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(100)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '1100100 10201 1210 400 244 202 144 121 100 91 84 79 72 6A 64')
    def test_Nr10_Zadanie_60_argumenty_1410(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(1410)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '10110000010 1221020 112002 21120 10310 4053 2602 1836 1410 1072 996 846 72A 640 582')
    def test_Nr11_Zadanie_60_argumenty_2004(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(2004)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '11111010100 2202020 133110 31004 13140 5562 3724 2666 2004 1562 11B0 BB2 A32 8D9 7D4')
    def test_Nr12_Zadanie_60_argumenty_24125(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(24125)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '101111000111101 1020002112 11320331 1233000 303405 130223 57075 36075 24125 17142 11B65 AC9A 8B13 7235 5E3D')
    def test_Nr13_Zadanie_60_argumenty_12591827(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(12591827)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '110000000010001011010011 212200201201222 300002023103 11210414302 1125515255 212012603 60021323 25621658 12591827 7120476 4272B2B 27BB4B1 195AC03 118ADA2 C022D3')
    def test_Nr14_Zadanie_60_argumenty_1251233(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(1251233)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '100110001011110100001 2100120100222 10301132201 310014413 42452425 13430624 4613641 2316328 1251233 785085 504115 34A699 247DBB 19AB08 1317A1')
    def test_Nr15_Zadanie_60_argumenty_2115(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_60(2115)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, '100001000011 2220100 201003 31430 13443 6111 4103 2810 2115 1653 1283 C69 AB1 960 843')

