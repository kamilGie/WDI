import unittest
import os
import sys
import importlib

from szablon1a2023 import zgodne


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

    def test_Nr01_zgodne_argumenty_tablica(self):
        wynik = zgodne([0])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr02_zgodne_argumenty_tablica(self):
        wynik = zgodne([6, 24])

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr03_zgodne_argumenty_tablica(self):
        wynik = zgodne([4, 6, 7, 9])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr04_zgodne_argumenty_tablica(self):
        wynik = zgodne([6, 12, 18, 24])

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr05_zgodne_argumenty_tablica(self):
        wynik = zgodne([3, 5, 7, 11, 13])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr06_zgodne_argumenty_tablica(self):
        wynik = zgodne([6, 6, 12, 12])

        oczekiwany_wynik = [4]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr07_zgodne_argumenty_tablica(self):
        wynik = zgodne([999, 996, 1000])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr08_zgodne_argumenty_tablica(self):
        wynik = zgodne([2, 4, 8, 16, 32])

        oczekiwany_wynik = [5]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr09_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                6,
                12,
                18,
                24,
                30,
                36,
                42,
                48,
                54,
                60,
                66,
                72,
                78,
                84,
                90,
                96,
                102,
                108,
                114,
                120,
                126,
                132,
                138,
                144,
                150,
            ]
        )

        oczekiwany_wynik = [9]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                2,
                4,
                6,
                8,
                10,
                15,
                20,
                30,
                45,
                60,
                70,
                80,
                90,
                100,
                120,
                130,
                140,
                150,
                160,
                180,
                200,
                210,
                220,
                240,
                300,
            ]
        )

        oczekiwany_wynik = [17]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                3,
                9,
                27,
                81,
                243,
                5,
                10,
                15,
                25,
                50,
                7,
                14,
                21,
                28,
                35,
                11,
                22,
                33,
                44,
                55,
                13,
                39,
                117,
                78,
                39,
            ]
        )

        oczekiwany_wynik = [12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr12_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                2,
                6,
                10,
                15,
                21,
                35,
                42,
                70,
                105,
                140,
                12,
                24,
                36,
                48,
                60,
                18,
                54,
                81,
                108,
                135,
                30,
                60,
                90,
                120,
                150,
            ]
        )

        oczekiwany_wynik = [14]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr13_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                1,
                2,
                4,
                8,
                16,
                32,
                64,
                128,
                256,
                512,
                3,
                9,
                27,
                81,
                243,
                5,
                25,
                125,
                625,
                500,
                15,
                45,
                90,
                135,
                270,
            ]
        )

        oczekiwany_wynik = [23]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr14_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ]
        )

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr15_zgodne_argumenty_tablica(self):
        wynik = zgodne(
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
                101,
                103,
                107,
                109,
                113,
                127,
                131,
                137,
                139,
                149,
                151,
                157,
                163,
                167,
                173,
                179,
                181,
                191,
                193,
                197,
                199,
                211,
                223,
                227,
                229,
                233,
                239,
                241,
                251,
                257,
                263,
                269,
                271,
                277,
                281,
                283,
                293,
                307,
                311,
                313,
                317,
                331,
                337,
                347,
                349,
                353,
                359,
                367,
                373,
                379,
                383,
                389,
                397,
                401,
                409,
                419,
                421,
                431,
                433,
                439,
                443,
                449,
                457,
                461,
                463,
                467,
                479,
                487,
                491,
                499,
                503,
                509,
                521,
                523,
                541,
            ]
        )

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)
