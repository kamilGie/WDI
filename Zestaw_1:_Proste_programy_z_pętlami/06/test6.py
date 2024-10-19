import unittest
import io
from contextlib import redirect_stdout

from exercise6 import Zadanie_6

TESTY = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test6(unittest.TestCase):

    def test_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "0"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(2)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(4)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "2"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(8)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "2"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_52(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(52)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "7"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "10"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_48(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(48)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "6"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(123)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "11"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_9(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(9)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_15(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(15)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "3"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_16(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(16)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "4"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_25(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(25)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "5"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_50(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(50)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "7"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_144(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(144)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "12"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_225(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(225)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "15"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_500(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(500)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "22"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_999(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(999)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "31"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_1024(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_6(1024)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "32"
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test6)
    unittest.TextTestRunner(verbosity=2).run(suite)
