import unittest
import sys
import io

from exercise110 import Zadanie_110

TESTY = False  # po napisaniu testow zmienic na true

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly


class Test110(unittest.TestCase):

    def test_wypisywania(self):
        # te komendy przejmuja wyniki printa
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_110()

        # przestajemy przejmowac wyniki printa i zwracamy jakie zmienne wypisalo po odpaleniu funkcji
        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()

        prawdziwyWynik = ""
        self.assertEqual(wynik, prawdziwyWynik)

    def test_zwracania(self):
        wynik = Zadanie_110()
        prawdziwyWynik = None
        self.assertEqual(wynik, prawdziwyWynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test110)
    unittest.TextTestRunner(verbosity=2).run(suite)
