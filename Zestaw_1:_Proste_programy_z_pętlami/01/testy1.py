import unittest
import io
from contextlib import redirect_stdout

from szablon1 import Zadanie_1

TESTY_ISTNIEJA = True  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
# oczekiwne wyniki sa w tablicy zeby moc akceptowac kilka mozliwych dobrych wynikow w roznej kolejnosci/formacie np ["(1,2)","1 2","1\n2\n"]
# print(f"{repr(wynik)}") # Przydaje sie, wyświetla wynik wraz z niewidocznymi znakami (np"\t1\n2\n3\n") gotowe do wklejenia do oczekiwanego_wyniku
class Testy1(unittest.TestCase):

    # zaczynam od przedrostka test i daje znaczaca nazwe
    def test_n_mnijesze_6(self):
        # przekierowywuje printa z terminala do zmiennej f
        f = io.StringIO()
        with redirect_stdout(f):
            # odpalam funkcje ktorych wynik bede chcial przewidziec
            Zadanie_1(0)
            Zadanie_1(1)
            Zadanie_1(2)
            Zadanie_1(3)
            Zadanie_1(4)
            Zadanie_1(5)
        wynik = f.getvalue().strip()

        # wpisuje oczekiwany wynik
        oczekiwany_wynik = [""]
        # wynik jest pusty bo po wszystkich wywolaniach od poczatku do konca nie ma rozwiazan
        self.assertIn(wynik, oczekiwany_wynik)

    def test_n_rowne_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(6)
        wynik = f.getvalue().strip()

        # Wynik to tablica, ponieważ użytkownik może zwrócić wartości w formacie print(int int float) lub print(int int int), więc przyjmujemy oba przypadki.
        oczekiwany_wynik = ["3 4 5", "3 4 5.0"]
        # nie jest to wymagane by tak robic dla typow zmiennych
        # mozna dodac do szablonu pod trescia forme jak ma zwrocic tak jak jest w tym szablonie (szablon1.py)
        # ale czasami kolejnsoci mozne np nie miec znaczenia i wtedy trzeba tutaj dac te kombinacje wszystkie do tablicy :,)
        # wiec jest to tylko przyklad pokazowy
        self.assertIn(wynik, oczekiwany_wynik)

    def test_n_rowne_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = ["3 4 5", "3 4 5.0"]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_n_rowne_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_1(100)
        wynik = f.getvalue().strip()
        # print(f"{repr(wynik)}") w takich przypadkach sie ten print przydaje
        # odpalam sprawdzma co mi wypisal tutaj i przekopiowuje z terminala do tablicy

        # no jest to brzydkie lepiej napisac na szablonie uzytkonwikowi jak ma wypisywac print(int(a) int(b) int(c))
        oczekiwany_wynik = [
            "3 4 5.0\n5 12 13.0\n6 8 10.0\n7 24 25.0\n8 15 17.0\n9 12 15.0\n9 40 41.0\n10 24 26.0\n11 60 61.0\n12 16 20.0\n12 35 37.0\n13 84 85.0\n14 48 50.0\n15 20 25.0\n15 36 39.0\n16 30 34.0\n16 63 65.0\n18 24 30.0\n18 80 82.0\n20 21 29.0\n20 48 52.0\n21 28 35.0\n21 72 75.0\n24 32 40.0\n24 45 51.0\n24 70 74.0\n25 60 65.0\n27 36 45.0\n28 45 53.0\n30 40 50.0\n30 72 78.0\n32 60 68.0\n33 44 55.0\n33 56 65.0\n35 84 91.0\n36 48 60.0\n36 77 85.0\n39 52 65.0\n39 80 89.0\n40 42 58.0\n40 75 85.0\n42 56 70.0\n45 60 75.0\n48 55 73.0\n48 64 80.0\n51 68 85.0\n54 72 90.0\n57 76 95.0\n60 63 87.0\n65 72 97.0",
            "3 4 5\n5 12 13\n6 8 10\n7 24 25\n8 15 17\n9 12 15\n9 40 41\n10 24 26\n11 60 61\n12 16 20\n12 35 37\n13 84 85\n14 48 50\n15 20 25\n15 36 39\n16 30 34\n16 63 65\n18 24 30\n18 80 82\n20 21 29\n20 48 52\n21 28 35\n21 72 75\n24 32 40\n24 45 51\n24 70 74\n25 60 65\n27 36 45\n28 45 53\n30 40 50\n30 72 78\n32 60 68\n33 44 55\n33 56 65\n35 84 91\n36 48 60\n36 77 85\n39 52 65\n39 80 89\n40 42 58\n40 75 85\n42 56 70\n45 60 75\n48 55 73\n48 64 80\n51 68 85\n54 72 90\n57 76 95\n60 63 87\n65 72 97",
        ]
        self.assertIn(wynik, oczekiwany_wynik)

    # nic nie zwracamy wiec rownie dobrze mozna to wywalic ale mozna tez zostawic i bedzie przechodzic
    def test_zwracania(self):
        # pod warunkiem ze albo nie mamy zadnej zmiennej albo damy tutaj losowa
        wynik = Zadanie_1(69)

        oczekiwany_wynik = [None]
        self.assertIn(wynik, oczekiwany_wynik)

    # tak samo zadziala wypisywania jak sprawdzamy zwracanie
    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            # sprawdze 0 bo nic nie wypisuje tak jak funkcja ktora nic nie wypisuje
            Zadanie_1(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY_ISTNIEJA, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Testy1)
    unittest.TextTestRunner(verbosity=2).run(suite)
