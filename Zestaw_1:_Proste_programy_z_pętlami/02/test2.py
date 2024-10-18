from contextlib import redirect_stdout
import unittest
import io

from exercise2 import Zadanie_2

TESTY = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test2(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_2()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n89\n144\n233\n377\n610\n987\n1597\n2584\n4181\n6765\n10946\n17711\n28657\n46368\n75025\n121393\n196418\n317811\n514229\n832040"
        self.assertEqual(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test2)
    unittest.TextTestRunner(verbosity=2).run(suite)
