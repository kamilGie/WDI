import unittest
from exercise4 import Zadanie_4

TESTY = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
class Test4(unittest.TestCase):

    def test_zwracania1(self):
        self.assertTrue(Zadanie_4(1))

    def test_zwracania9(self):
        self.assertFalse(Zadanie_4(9))

    def test_zwracania2(self):
        self.assertTrue(Zadanie_4(2))

    def test_zwracania843(self):
        self.assertTrue(Zadanie_4(843))

    def test_zwracania377(self):
        self.assertTrue(Zadanie_4(377))

    def test_zwracania987(self):
        self.assertTrue(Zadanie_4(987))

    def test_zwracania26(self):
        self.assertTrue(Zadanie_4(26))

    def test_zwracania100(self):
        self.assertFalse(Zadanie_4(100))

    def test_zwracania2115(self):
        self.assertFalse(Zadanie_4(2115))

    def test_zwracania12345(self):
        self.assertFalse(Zadanie_4(12345))

    def test_zwracania5000(self):
        self.assertFalse(Zadanie_4(5000))


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test4)
    unittest.TextTestRunner(verbosity=2).run(suite)
