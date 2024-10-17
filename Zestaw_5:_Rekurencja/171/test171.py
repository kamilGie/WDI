import unittest
import sys
import io

from exercise171 import Zadanie_171

TESTY = False  # po napisaniu testow zmienic na true

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly


class Test171(unittest.TestCase):

    def test_wypisywania(self):
        # te komendy przejmuja wyniki printa
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_171()

        # przestajemy przejmowac wyniki printa i zwracamy jakie zmienne wypisalo po odpaleniu funkcji
        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()

        prawdziwyWynik = ""
        self.assertEqual(wynik, prawdziwyWynik)

    def test_zwracania(self):
        wynik = Zadanie_171()
        prawdziwyWynik = None
        self.assertEqual(wynik, prawdziwyWynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test171)
    unittest.TextTestRunner(verbosity=2).run(suite)
