import unittest
import os
import sys
import importlib

from szablon0_2020 import multi


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_multi_argumenty_tablica(self):
        wynik = multi(["ABCABCABC", "AAAA", "ABAABA", "DEF"])

        oczekiwany_wynik = [9]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr2_multi_argumenty_tablica(self):
        wynik = multi(["AB", "CD", "EFG", "HIJK"])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr3_multi_argumenty_tablica(self):
        wynik = multi(["AAAAA", "BB", "CCC", "D", "EEEEE"])

        oczekiwany_wynik = [5]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr4_multi_argumenty_tablica(self):
        wynik = multi(["XYZXYZ", "LLL", "MNMNMNMN", "OOO"])

        oczekiwany_wynik = [8]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr5_multi_argumenty_tablica(self):
        wynik = multi(["A", "B", "C", "D"])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr6_multi_argumenty_tablica(self):
        wynik = multi(["ABABABAB", "CDCDCDCDCDCD", "EFEFEF"])

        oczekiwany_wynik = [12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr7_multi_argumenty_tablica(self):
        wynik = multi([""])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr8_multi_argumenty_tablica(self):
        wynik = multi(["ZZZZZZZZZ"])

        oczekiwany_wynik = [9]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr9_multi_argumenty_tablica(self):
        wynik = multi(["HELLO", "WORLD", "AAA", "AAA", "ABCABC", "XYZXYZXYZ"])

        oczekiwany_wynik = [9]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr10_multi_argumenty_tablica(self):
        wynik = multi(["123123123123", "ABABABABAB", "XYXYXY", "99999999", "456456"])

        oczekiwany_wynik = [12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr11_multi_argumenty_tablica(self):
        wynik = multi(["ABABABABABAB", "XYZXYZ", "HIHIHI", "NOPQRS", "ABCDABCD"])

        oczekiwany_wynik = [12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr12_multi_argumenty_tablica(self):
        wynik = multi(["ABCDABCDABCDX", "XYZXYZYZZ", "AAAAAAB", "123123124"])

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr13_multi_argumenty_tablica(self):
        wynik = multi(["ABCAABCAABCA", "1234123412345", "XYYXYYXYYX"])

        oczekiwany_wynik = [12]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr14_multi_argumenty_tablica(self):
        wynik = multi(["AA"])

        oczekiwany_wynik = [2]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr15_multi_argumenty_tablica(self):
        wynik = multi(
            [
                "AB",
                "BA",
                "AC",
                "CA",
                "AD",
                "DA",
                "BC",
                "CB",
                "BD",
                "DB",
                "CD",
                "DC",
                "EF",
                "FE",
                "EG",
                "GE",
                "EH",
                "HE",
                "FG",
                "GF",
                "FH",
                "HF",
                "GH",
                "HG",
                "IJ",
                "JI",
                "IK",
                "KI",
                "IL",
                "LI",
                "JK",
                "KJ",
                "JL",
                "LJ",
                "KL",
                "LK",
                "MN",
                "NM",
                "MO",
                "OM",
                "MP",
                "PM",
                "NO",
                "ON",
                "NP",
                "PN",
                "OP",
                "PO",
                "QR",
                "RQ",
                "QS",
                "SQ",
                "QT",
                "TQ",
                "RS",
                "SR",
                "RT",
                "TR",
                "ST",
                "TS",
                "UV",
                "VU",
                "UW",
                "WU",
                "UX",
                "XU",
                "VW",
                "WV",
                "VX",
                "XV",
                "WX",
                "XW",
                "YZ",
                "ZY",
                "YA",
                "AY",
                "YB",
                "BY",
                "ZA",
                "AZ",
                "ZB",
                "BZ",
                "AB",
                "BA",
            ]
        )

        oczekiwany_wynik = [0]
        self.assertIn(wynik, oczekiwany_wynik)
