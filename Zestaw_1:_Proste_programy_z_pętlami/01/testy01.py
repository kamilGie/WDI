import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon01 import Zadanie_1


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
    skrypty_dir = os.path.join(
        os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty"
    )
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_Zadanie_1_argumenty_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_Zadanie_1_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_Zadanie_1_argumenty_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_Zadanie_1_argumenty_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(5)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_Zadanie_1_argumenty_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(6)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ["3 4 5"]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_Zadanie_1_argumenty_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ["3 4 5"]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_Zadanie_1_argumenty_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(20)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ["3 4 5\n5 12 13\n6 8 10\n8 15 17\n9 12 15"]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_Zadanie_1_argumenty_40(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(40)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [
            "3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n10 24 26\n12 16 20\n12 35 37\n15 20 25\n15 36 39\n16 30 34\n18 24 30\n20 21 29\n21 28 35"
        ]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_Zadanie_1_argumenty_80(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(80)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [
            "3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n14 48 50\n15 20 25\n15 36 39\n16 30 34\n16 63 65\n18 24 30\n20 21 29\n20 48 52\n21 28 35\n21 72 75\n24 32 40\n24 45 51\n24 70 74\n25 60 65\n27 36 45\n28 45 53\n30 40 50\n30 72 78\n32 60 68\n33 44 55\n33 56 65\n36 48 60\n39 52 65\n40 42 58\n42 56 70\n45 60 75\n48 55 73"
        ]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_Zadanie_1_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [
            "3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n13 84 85\n14 48 50\n15 20 25\n15 36 39\n16 30 34\n16 63 65\n18 24 30\n18 80 82\n20 21 29\n20 48 52\n21 28 35\n21 72 75\n24 32 40\n24 45 51\n24 70 74\n25 60 65\n27 36 45\n28 45 53\n30 40 50\n30 72 78\n32 60 68\n33 44 55\n33 56 65\n35 84 91\n36 48 60\n36 77 85\n39 52 65\n39 80 89\n40 42 58\n40 75 85\n42 56 70\n45 60 75\n48 55 73\n48 64 80\n51 68 85\n54 72 90\n57 76 95\n60 63 87\n65 72 97"
        ]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_Zadanie_1_argumenty_140(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(140)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [
            "3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n13 84 85\n14 48 50\n15 20 25\n15 36 39\n15 112 113\n16 30 34\n16 63 65\n18 24 30\n18 80 82\n20 21 29\n20 48 52\n20 99 101\n21 28 35\n21 72 75\n22 120 122\n24 32 40\n24 45 51\n24 70 74\n25 60 65\n27 36 45\n27 120 123\n28 45 53\n28 96 100\n30 40 50\n30 72 78\n32 60 68\n32 126 130\n33 44 55\n33 56 65\n35 84 91\n35 120 125\n36 48 60\n36 77 85\n36 105 111\n39 52 65\n39 80 89\n40 42 58\n40 75 85\n40 96 104\n42 56 70\n44 117 125\n45 60 75\n45 108 117\n48 55 73\n48 64 80\n48 90 102\n50 120 130\n51 68 85\n54 72 90\n56 90 106\n56 105 119\n57 76 95\n60 63 87\n60 80 100\n60 91 109\n63 84 105\n64 120 136\n65 72 97\n66 88 110\n66 112 130\n69 92 115\n72 96 120\n75 100 125\n78 104 130\n80 84 116\n81 108 135\n88 105 137"
        ]
        self.assertIn(wynik, oczekiwany_wynik)
