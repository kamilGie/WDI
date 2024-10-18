import unittest
<<<<<<< HEAD
from contextlib import redirect_stdout
=======
>>>>>>> upstream/solutions
import io
from contextlib import redirect_stdout

from exercise2 import Zadanie_2

TESTY = False  # po napisaniu testow zmienic na true

<<<<<<< HEAD
# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
=======

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
>>>>>>> upstream/solutions
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test2(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_2()
        wynik = f.getvalue().strip()

<<<<<<< HEAD
        prawdziwyWynik = ""
        self.assertEqual(wynik, prawdziwyWynik)
=======
        oczekiwany_wynik = ""
        self.assertEqual(wynik, oczekiwany_wynik)
>>>>>>> upstream/solutions

    def test_zwracania(self):
        wynik = Zadanie_2()

        oczekiwany_wynik = None
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test2)
    unittest.TextTestRunner(verbosity=2).run(suite)
