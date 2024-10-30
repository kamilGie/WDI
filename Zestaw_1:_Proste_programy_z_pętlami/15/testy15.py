import unittest
import os
import sys
import importlib

from szablon15 import nwd3


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

    def test_Nr1_nwd3_argumenty_1_1_1(self):
        wynik = nwd3(1, 1, 1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_nwd3_argumenty_4_4_4(self):
        wynik = nwd3(4, 4, 4)

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_nwd3_argumenty_60_30_105(self):
        wynik = nwd3(60, 30, 105)

        oczekiwany_wynik = [15]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_nwd3_argumenty_100_0_25(self):
        wynik = nwd3(100, 0, 25)

        oczekiwany_wynik = [25]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_nwd3_argumenty_101_103_107(self):
        wynik = nwd3(101, 103, 107)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_nwd3_argumenty_144_96_36(self):
        wynik = nwd3(144, 96, 36)

        oczekiwany_wynik = [12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_nwd3_argumenty_1200_1800_2400(self):
        wynik = nwd3(1200, 1800, 2400)

        oczekiwany_wynik = [600]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_nwd3_argumenty_9999991_9999992_9999993(self):
        wynik = nwd3(9999991, 9999992, 9999993)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_nwd3_argumenty_1024_2048_3072(self):
        wynik = nwd3(1024, 2048, 3072)

        oczekiwany_wynik = [1024]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_nwd3_argumenty_10000_25000_40000(self):
        wynik = nwd3(10000, 25000, 40000)

        oczekiwany_wynik = [5000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_nwd3_argumenty_1357_2469_3691(self):
        wynik = nwd3(1357, 2469, 3691)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr12_nwd3_argumenty_16_64_256(self):
        wynik = nwd3(16, 64, 256)

        oczekiwany_wynik = [16]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr13_nwd3_argumenty_200_300_400(self):
        wynik = nwd3(200, 300, 400)

        oczekiwany_wynik = [100]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr14_nwd3_argumenty_9876_5432_1234(self):
        wynik = nwd3(9876, 5432, 1234)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr15_nwd3_argumenty_102043_102359_101807(self):
        wynik = nwd3(102043, 102359, 101807)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr16_nwd3_argumenty_23423_324234_2342(self):
        wynik = nwd3(23423, 324234, 2342)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr17_nwd3_argumenty_234_242_3234(self):
        wynik = nwd3(234, 242, 3234)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr18_nwd3_argumenty_234_52312_12(self):
        wynik = nwd3(234, 52312, 12)

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr19_nwd3_argumenty_123_421_1(self):
        wynik = nwd3(123, 421, 1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr20_nwd3_argumenty_123_123_246(self):
        wynik = nwd3(123, 123, 246)

        oczekiwany_wynik = [123]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr21_nwd3_argumenty_213_45612_12323(self):
        wynik = nwd3(213, 45612, 12323)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr22_nwd3_argumenty_321_324_123(self):
        wynik = nwd3(321, 324, 123)

        oczekiwany_wynik = [3]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr23_nwd3_argumenty_123_1230_2110(self):
        wynik = nwd3(123, 1230, 2110)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr24_nwd3_argumenty_10000_20000_30000(self):
        wynik = nwd3(10000, 20000, 30000)

        oczekiwany_wynik = [10000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr25_nwd3_argumenty_999_1111_2222(self):
        wynik = nwd3(999, 1111, 2222)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr26_nwd3_argumenty_1001_1003_1005(self):
        wynik = nwd3(1001, 1003, 1005)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr27_nwd3_argumenty_96000_128000_160000(self):
        wynik = nwd3(96000, 128000, 160000)

        oczekiwany_wynik = [32000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr28_nwd3_argumenty_10000_20000_30000(self):
        wynik = nwd3(10000, 20000, 30000)

        oczekiwany_wynik = [10000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr29_nwd3_argumenty_15000_30000_45000(self):
        wynik = nwd3(15000, 30000, 45000)

        oczekiwany_wynik = [15000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr30_nwd3_argumenty_24000_36000_48000(self):
        wynik = nwd3(24000, 36000, 48000)

        oczekiwany_wynik = [12000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr31_nwd3_argumenty_12000_18000_24000(self):
        wynik = nwd3(12000, 18000, 24000)

        oczekiwany_wynik = [6000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr32_nwd3_argumenty_50000_100000_150000(self):
        wynik = nwd3(50000, 100000, 150000)

        oczekiwany_wynik = [50000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr33_nwd3_argumenty_80000_120000_160000(self):
        wynik = nwd3(80000, 120000, 160000)

        oczekiwany_wynik = [40000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr34_nwd3_argumenty_150000_225000_300000(self):
        wynik = nwd3(150000, 225000, 300000)

        oczekiwany_wynik = [75000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr35_nwd3_argumenty_30000_90000_150000(self):
        wynik = nwd3(30000, 90000, 150000)

        oczekiwany_wynik = [30000]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr36_nwd3_argumenty_48000_72000_96000(self):
        wynik = nwd3(48000, 72000, 96000)

        oczekiwany_wynik = [24000]
        self.assertIn(wynik, oczekiwany_wynik)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr59_nwd3_argumenty_0_0_0(self):
        wynik = nwd3(0, 0, 0)

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr60_nwd3_argumenty_0_1_1(self):
        wynik = nwd3(0, 1, 1)

        oczekiwany_wynik = [1]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr61_nwd3_argumenty_0_0_123123(self):
        wynik = nwd3(0, 0, 123123)

        oczekiwany_wynik = [123123]
        self.assertIn(wynik, oczekiwany_wynik)
