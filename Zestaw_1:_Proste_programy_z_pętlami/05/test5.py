import unittest
import io
from contextlib import redirect_stdout

from exercise5 import Zadanie_5

TESTY = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test5(unittest.TestCase):

    def test_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(2)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(4)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "2"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(8)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "2"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_52(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(52)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "7"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "10"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_48(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(48)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "6"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_5(123)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "11"
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test5)
    unittest.TextTestRunner(verbosity=2).run(suite)
