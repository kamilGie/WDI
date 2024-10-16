import unittest
import sys
import io
import os
import importlib

# Dodanie dynamicznej ścieżki do katalogu nadrzędnego
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(current_dir, os.pardir)))
Zadanie_1 = importlib.import_module("01").Zadanie_1

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly


class Test_1(unittest.TestCase):
    def test_nRowne1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_1(1)

        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()

        prawdziwyWynik = ""
        self.assertEqual(wynik, prawdziwyWynik)

    def test_n_rowne_2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_1(2)

        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()

        prawdziwyWynik = "1 1 1"
        self.assertEqual(wynik, prawdziwyWynik)

    def test_n_rowne_3(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_1(3)

        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()

        prawdziwyWynik = "1 1 1\n1 1 2\n1 2 1\n1 2 2\n2 1 1\n2 1 2\n2 2 1\n2 2 2"
        self.assertEqual(wynik, prawdziwyWynik)

    def test_n_rowne_4(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        Zadanie_1(4)

        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()
        prawdziwyWynik = "1 1 1\n1 1 2\n1 1 3\n1 2 1\n1 2 2\n1 2 3\n1 3 1\n1 3 2\n1 3 3\n2 1 1\n2 1 2\n2 1 3\n2 2 1\n2 2 2\n2 2 3\n2 3 1\n2 3 2\n2 3 3\n3 1 1\n3 1 2\n3 1 3\n3 2 1\n3 2 2\n3 2 3\n3 3 1\n3 3 2\n3 3 3"
        self.assertEqual(wynik, prawdziwyWynik)

    def test_zwracajacy(self):
        wynik = Zadanie_1(2)
        prawdziwyWynik = None
        self.assertEqual(wynik, prawdziwyWynik)


if __name__ == "__main__":
    unittest.main()
