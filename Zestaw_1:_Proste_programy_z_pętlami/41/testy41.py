import unittest
import os
import sys
import importlib

from szablon41 import Zadanie_41


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

    def test_Nr01_Zadanie_41_argumenty_1(self):
        self.assertEqual(Zadanie_41(1), 1)

    def test_Nr02_Zadanie_41_argumenty_5(self):
        self.assertEqual(Zadanie_41(5), 2)

    def test_Nr03_Zadanie_41_argumenty_10(self):
        self.assertEqual(Zadanie_41(10), 8)

    def test_Nr04_Zadanie_41_argumenty_24(self):
        self.assertEqual(Zadanie_41(24), 6)

    def test_Nr05_Zadanie_41_argumenty_25(self):
        self.assertEqual(Zadanie_41(25), 4)

    def test_Nr06_Zadanie_41_argumenty_30(self):
        self.assertEqual(Zadanie_41(30), 8)

    def test_Nr07_Zadanie_41_argumenty_45(self):
        self.assertEqual(Zadanie_41(45), 6)

    def test_Nr08_Zadanie_41_argumenty_60(self):
        self.assertEqual(Zadanie_41(60), 6)

    def test_Nr09_Zadanie_41_argumenty_100(self):
        self.assertEqual(Zadanie_41(100), 4)

    def test_Nr10_Zadanie_41_argumenty_123(self):
        self.assertEqual(Zadanie_41(123), 6)

    def test_Nr11_Zadanie_41_argumenty_150(self):
        self.assertEqual(Zadanie_41(150), 2)

    def test_Nr12_Zadanie_41_argumenty_250(self):
        self.assertEqual(Zadanie_41(250), 8)

    def test_Nr13_Zadanie_41_argumenty_500(self):
        self.assertEqual(Zadanie_41(500), 4)

    def test_Nr14_Zadanie_41_argumenty_1001(self):
        self.assertEqual(Zadanie_41(1001), 2)

    def test_Nr15_Zadanie_41_argumenty_2004(self):
        self.assertEqual(Zadanie_41(2004), 2)

    def test_Nr16_Zadanie_41_argumenty_5123(self):
        self.assertEqual(Zadanie_41(5123), 2)

    def test_Nr17_Zadanie_41_argumenty_7890(self):
        self.assertEqual(Zadanie_41(7890), 6)

    def test_Nr18_Zadanie_41_argumenty_10100(self):
        self.assertEqual(Zadanie_41(10100), 2)

    def test_Nr19_Zadanie_41_argumenty_2115(self):
        self.assertEqual(Zadanie_41(2115), 6)
