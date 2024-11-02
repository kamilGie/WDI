import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon27 import palindron_dziesietny, palindron_dwojkowy


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_palindron_dziesietny_argumenty_1(self):
        wynik  = palindron_dziesietny(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_palindron_dziesietny_argumenty_2(self):
        wynik  = palindron_dziesietny(2)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_palindron_dziesietny_argumenty_9(self):
        wynik  = palindron_dziesietny(9)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_palindron_dziesietny_argumenty_0(self):
        wynik  = palindron_dziesietny(0)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_palindron_dziesietny_argumenty_10(self):
        wynik  = palindron_dziesietny(10)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_palindron_dziesietny_argumenty_11(self):
        wynik  = palindron_dziesietny(11)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_palindron_dziesietny_argumenty_121(self):
        wynik  = palindron_dziesietny(121)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_palindron_dziesietny_argumenty_151(self):
        wynik  = palindron_dziesietny(151)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_palindron_dziesietny_argumenty_210(self):
        wynik  = palindron_dziesietny(210)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_palindron_dziesietny_argumenty_1410(self):
        wynik  = palindron_dziesietny(1410)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_palindron_dziesietny_argumenty_2112(self):
        wynik  = palindron_dziesietny(2112)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_palindron_dziesietny_argumenty_1510(self):
        wynik  = palindron_dziesietny(1510)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_palindron_dziesietny_argumenty_2000(self):
        wynik  = palindron_dziesietny(2000)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_palindron_dziesietny_argumenty_4545(self):
        wynik  = palindron_dziesietny(4545)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr15_palindron_dziesietny_argumenty_51115(self):
        wynik  = palindron_dziesietny(51115)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr16_palindron_dziesietny_argumenty_91219(self):
        wynik  = palindron_dziesietny(91219)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr17_palindron_dziesietny_argumenty_912191(self):
        wynik  = palindron_dziesietny(912191)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr18_palindron_dziesietny_argumenty_12345678900987654321(self):
        wynik  = palindron_dziesietny(12345678900987654321)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr19_palindron_dziesietny_argumenty_5432167805432167890(self):
        wynik  = palindron_dziesietny(5432167805432167890)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr01_palindron_dwojkowy_argumenty_1(self):
        wynik  = palindron_dwojkowy(1)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr02_palindron_dwojkowy_argumenty_2(self):
        wynik  = palindron_dwojkowy(2)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr03_palindron_dwojkowy_argumenty_4(self):
        wynik  = palindron_dwojkowy(4)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr04_palindron_dwojkowy_argumenty_1024(self):
        wynik  = palindron_dwojkowy(1024)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr05_palindron_dwojkowy_argumenty_1028(self):
        wynik  = palindron_dwojkowy(1028)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr06_palindron_dwojkowy_argumenty_2048(self):
        wynik  = palindron_dwojkowy(2048)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr07_palindron_dwojkowy_argumenty_2047(self):
        wynik  = palindron_dwojkowy(2047)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr08_palindron_dwojkowy_argumenty_1023(self):
        wynik  = palindron_dwojkowy(1023)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr09_palindron_dwojkowy_argumenty_21(self):
        wynik  = palindron_dwojkowy(21)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr10_palindron_dwojkowy_argumenty_27(self):
        wynik  = palindron_dwojkowy(27)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr11_palindron_dwojkowy_argumenty_31(self):
        wynik  = palindron_dwojkowy(31)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr12_palindron_dwojkowy_argumenty_105(self):
        wynik  = palindron_dwojkowy(105)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr13_palindron_dwojkowy_argumenty_111(self):
        wynik  = palindron_dwojkowy(111)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr14_palindron_dwojkowy_argumenty_99(self):
        wynik  = palindron_dwojkowy(99)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr15_palindron_dwojkowy_argumenty_123156(self):
        wynik  = palindron_dwojkowy(123156)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr16_palindron_dwojkowy_argumenty_131071(self):
        wynik  = palindron_dwojkowy(131071)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr17_palindron_dwojkowy_argumenty_1048575(self):
        wynik  = palindron_dwojkowy(1048575)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr18_palindron_dwojkowy_argumenty_1572865(self):
        wynik  = palindron_dwojkowy(1572865)

        oczekiwany_wynik = False
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr19_palindron_dwojkowy_argumenty_8388607(self):
        wynik  = palindron_dwojkowy(8388607)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr20_palindron_dwojkowy_argumenty_455(self):
        wynik  = palindron_dwojkowy(455)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)
    def test_Nr21_palindron_dwojkowy_argumenty_231(self):
        wynik  = palindron_dwojkowy(231)

        oczekiwany_wynik = True
        self.assertEqual(wynik, oczekiwany_wynik)

