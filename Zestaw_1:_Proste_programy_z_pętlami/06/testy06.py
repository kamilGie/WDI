import unittest
import os
import sys
import importlib

from szablon06 import Zadanie_6


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
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr2_Zadanie_6_argumenty_1(self):
        wynik = Zadanie_6(1)

        oczekiwany_wynik = 1.0
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr3_Zadanie_6_argumenty_3(self):
        wynik = Zadanie_6(3)

        oczekiwany_wynik = 1.7320508075688772
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr4_Zadanie_6_argumenty_4(self):
        wynik = Zadanie_6(4)

        oczekiwany_wynik = 2.000000000000002
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr5_Zadanie_6_argumenty_8(self):
        wynik = Zadanie_6(8)

        oczekiwany_wynik = 2.82842712474619
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr6_Zadanie_6_argumenty_9(self):
        wynik = Zadanie_6(9)

        oczekiwany_wynik = 3.0
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr7_Zadanie_6_argumenty_123(self):
        wynik = Zadanie_6(123)

        oczekiwany_wynik = 11.090536506409418
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr8_Zadanie_6_argumenty_5001(self):
        wynik = Zadanie_6(5001)

        oczekiwany_wynik = 70.71774883294859
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr9_Zadanie_6_argumenty_12345(self):
        wynik = Zadanie_6(12345)

        oczekiwany_wynik = 111.1080555135405
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr10_Zadanie_6_argumenty_4473225(self):
        wynik = Zadanie_6(4473225)

        oczekiwany_wynik = 2115.0
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)

    def test_Nr11_Zadanie_6_argumenty_1234567890(self):
        wynik = Zadanie_6(1234567890)

        oczekiwany_wynik = 35136.41828644462
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)
