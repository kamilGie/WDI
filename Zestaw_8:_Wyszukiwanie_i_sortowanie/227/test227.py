import unittest
import io
from contextlib import redirect_stdout

from exercise227 import Zadanie_227

TESTY = False  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test227(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_227()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_zwracania(self):
        wynik = Zadanie_227()

        oczekiwany_wynik = None
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test227)
    unittest.TextTestRunner(verbosity=2).run(suite)
