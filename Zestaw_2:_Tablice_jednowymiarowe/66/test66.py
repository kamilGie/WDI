import unittest
import io
from contextlib import redirect_stdout

from exercise66 import Zadanie_66

TESTY = False  # po napisaniu testow zmienic na true

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly


class Test66(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_66()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_zwracania(self):
        wynik = Zadanie_66()

        oczekiwany_wynik = None
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test66)
    unittest.TextTestRunner(verbosity=2).run(suite)