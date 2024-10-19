import unittest
import io
from contextlib import redirect_stdout

from exercise1 import Zadanie_1

TESTY = True  # po napisaniu testow zmienic na true


class Test1(unittest.TestCase):

    def test_n_mnijesze_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(0)
            Zadanie_1(1)
            Zadanie_1(2)
            Zadanie_1(3)
            Zadanie_1(4)
            Zadanie_1(5)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_n_rowne_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(6)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_n_rowne_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3 4 5"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_n_rowne_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(100)
        wynik = f.getvalue().strip()
        oczekiwany_wynik = "3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n13 84 85\n14 48 50\n15 20 25\n15 36 39\n16 30 34\n16 63 65\n18 24 30\n18 80 82\n20 21 29\n20 48 52\n21 28 35\n21 72 75\n24 32 40\n24 45 51\n24 70 74\n25 60 65\n27 36 45\n28 45 53\n30 40 50\n30 72 78\n32 60 68\n33 44 55\n33 56 65\n35 84 91\n36 48 60\n36 77 85\n39 52 65\n39 80 89\n40 42 58\n40 75 85\n42 56 70\n45 60 75\n48 55 73\n48 64 80\n51 68 85\n54 72 90\n57 76 95\n60 63 87\n65 72 97"
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    unittest.TextTestRunner(verbosity=2).run(suite)
