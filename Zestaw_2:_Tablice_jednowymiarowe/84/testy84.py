import unittest
import os
import sys
import importlib

from szablon84 import multi


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

    def test_Nr01_multi_argumenty_tablica(self):
        self.assertEqual(multi(["ABCABCABC", "AAAA", "ABAABA"]), 3)

    def test_Nr02_multi_argumenty_tablica(self):
        self.assertEqual(multi(["ABCD", "EFGH", "IJKL"]), 0)

    def test_Nr03_multi_argumenty_tablica(self):
        self.assertEqual(multi(["ABAB", "XYZXYZXYZ", "A"]), 3)

    def test_Nr04_multi_argumenty_tablica(self):
        self.assertEqual(multi(["ABCDE"]), 0)

    def test_Nr05_multi_argumenty_tablica(self):
        self.assertEqual(multi(["ZZZZZZZ"]), 1)

    def test_Nr06_multi_argumenty_tablica(self):
        self.assertEqual(multi(["ABCABC", "ABABAB", "XYZXYZXYZ"]), 3)

    def test_Nr07_multi_argumenty_tablica(self):
        self.assertEqual(multi(["AAB", "AABB", "BBAA", "ABABABAB"]), 4)

    def test_Nr08_multi_argumenty_tablica(self):
        self.assertEqual(multi(["LPLPLP", "PQR"]), 2)

    def test_Nr09_multi_argumenty_tablica(self):
        self.assertEqual(multi(["JJJJJJ", "IIII", "JJJJJJJJ"]), 4)

    def test_Nr10_multi_argumenty_tablica(self):
        self.assertEqual(multi(["POKEMOPKEMO", "COFFEECOFFEE"]), 6)

    def test_Nr11_multi_argumenty_tablica(self):
        self.assertEqual(multi(["X", "XX", "XXX", "XXXX"]), 2)

    def test_Nr12_multi_argumenty_tablica(self):
        self.assertEqual(multi(["HELLOHELLOHELLO", "WORDWORD"]), 5)

    def test_Nr13_multi_argumenty_tablica(self):
        self.assertEqual(multi(["XYZXYZXYZ", "TESTTESTTEST"]), 4)
