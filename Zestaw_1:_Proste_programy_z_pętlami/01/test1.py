import unittest
import io
from contextlib import redirect_stdout

from exercise1 import Zadanie_1

TESTY = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test1(unittest.TestCase):

    def test_n_rowne_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_n_rowne_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(2)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1 1 1"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_n_rowne_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1 1 1\n1 1 2\n1 2 1\n1 2 2\n2 1 1\n2 1 2\n2 2 1\n2 2 2"
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_n_rowne_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(4)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1 1 1\n1 1 2\n1 1 3\n1 2 1\n1 2 2\n1 2 3\n1 3 1\n1 3 2\n1 3 3\n2 1 1\n2 1 2\n2 1 3\n2 2 1\n2 2 2\n2 2 3\n2 3 1\n2 3 2\n2 3 3\n3 1 1\n3 1 2\n3 1 3\n3 2 1\n3 2 2\n3 2 3\n3 3 1\n3 3 2\n3 3 3"
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    unittest.TextTestRunner(verbosity=2).run(suite)
