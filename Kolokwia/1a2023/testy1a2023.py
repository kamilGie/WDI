import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon1a2023 import zgodne


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2).run(suite)


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
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_zgodne_argumenty_t2_3_4_5_7_6_23_24_12_13_14_15_16_45t(self):
        wynik  = zgodne([2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45])

        oczekiwany_wynik = [7]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr2_zgodne_argumenty_t10_15_20_25_30_35_50_75_90_100t(self):
        wynik  = zgodne([10, 15, 20, 25, 30, 35, 50, 75, 90, 100])

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr3_zgodne_argumenty_t2_3_6_9_11_12_15_18_21_24_30t(self):
        wynik  = zgodne([2, 3, 6, 9, 11, 12, 15, 18, 21, 24, 30])

        oczekiwany_wynik = [5]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr4_zgodne_argumenty_t4_8_12_16_20_24_28_32_36_40_44t(self):
        wynik  = zgodne([4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

        oczekiwany_wynik = [3]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr5_zgodne_argumenty_t10_21_14_28_22_33_44_77_88_99t(self):
        wynik  = zgodne([10, 21, 14, 28, 22, 33, 44, 77, 88, 99])

        oczekiwany_wynik = [5]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr6_zgodne_argumenty_t6_12_24_18_30_36_42_48_54_60t(self):
        wynik  = zgodne([6, 12, 24, 18, 30, 36, 42, 48, 54, 60])

        oczekiwany_wynik = [7]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr7_zgodne_argumenty_t3_5_7_9_14_15_16_18_2_4_8_10t(self):
        wynik  = zgodne([3, 5, 7, 9, 14, 15, 16, 18, 2, 4, 8, 10])

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr8_zgodne_argumenty_t10_21_14_28_22_33_44_77_88_99_100_110_120_130_140_150_160_170_180_190_200t(self):
        wynik  = zgodne([10, 21, 14, 28, 22, 33, 44, 77, 88, 99, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])

        oczekiwany_wynik = [5]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr9_zgodne_argumenty_t6_12_24_18_30_36_42_48_54_60_66_72_78_84_90_96_102_108_114_120t(self):
        wynik  = zgodne([6, 12, 24, 18, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120])

        oczekiwany_wynik = [9]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr10_zgodne_argumenty_t2_5_8_10_15_18_20_25_30_35_40_45_50_55_60_65_70_75_80_85_90_95_100_105_110_115_120_125_130_135_140_145_150_155_160_165_170_175_180_185_190_195_200_205_210_215_220_225_230_235_240_245_250_255_260_265_270_275_280_285_290_295_300_305_310_315_320_325_330_335_340_345_350_355_360_365_370_375_380_385_390_395_400t(self):
        wynik  = zgodne([2, 5, 8, 10, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400])

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)
    def test_Nr11_zgodne_argumenty_t2_3_5_7_11_13_17_19_23_29_31_37_41_43_47_53_59_61_67_71_73_79_83_89_97_101_103_107_109_113_127_131_137_139_149_151_157_163_167_173_179_181_191_193_197_199_211_223_227_229_233_239_241_251_257_263_269_271_277_281_283_293_307_311_313_317_331_337_347_349_353_359_367_373_379_383_389_397_401t(self):
        wynik  = zgodne([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

