import unittest
import os
import sys
import importlib


from szablon0_2020 import silnia


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_silnia_argumenty_1(self):
        wynik = silnia(1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr02_silnia_argumenty_2(self):
        wynik = silnia(2)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr03_silnia_argumenty_4(self):
        wynik = silnia(4)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr04_silnia_argumenty_5(self):
        wynik = silnia(5)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr05_silnia_argumenty_3(self):
        wynik = silnia(3)

        oczekiwany_wynik = [6]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr06_silnia_argumenty_6(self):
        wynik = silnia(6)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr07_silnia_argumenty_7(self):
        wynik = silnia(7)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr08_silnia_argumenty_8(self):
        wynik = silnia(8)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr09_silnia_argumenty_9(self):
        wynik = silnia(9)

        oczekiwany_wynik = [8]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_silnia_argumenty_10(self):
        wynik = silnia(10)

        oczekiwany_wynik = [8]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_silnia_argumenty_11(self):
        wynik = silnia(11)

        oczekiwany_wynik = [8]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr12_silnia_argumenty_20(self):
        wynik = silnia(20)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr13_silnia_argumenty_40(self):
        wynik = silnia(40)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr14_silnia_argumenty_100(self):
        wynik = silnia(100)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr15_silnia_argumenty_200(self):
        wynik = silnia(200)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr16_silnia_argumenty_500(self):
        wynik = silnia(500)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr17_silnia_argumenty_1410(self):
        wynik = silnia(1410)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr18_silnia_argumenty_1600(self):
        wynik = silnia(1600)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr19_silnia_argumenty_200(self):
        wynik = silnia(200)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr20_silnia_argumenty_2000(self):
        wynik = silnia(2000)

        oczekiwany_wynik = [8]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr21_silnia_argumenty_2004(self):
        wynik = silnia(2004)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr22_silnia_argumenty_2400(self):
        wynik = silnia(2400)

        oczekiwany_wynik = [6]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr23_silnia_argumenty_2999(self):
        wynik = silnia(2999)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr24_silnia_argumenty_3000(self):
        wynik = silnia(3000)

        oczekiwany_wynik = [6]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr25_silnia_argumenty_2115(self):
        wynik = silnia(2115)

        oczekiwany_wynik = [6]
        self.assertIn(wynik, oczekiwany_wynik)
