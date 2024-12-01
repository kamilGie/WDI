import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon149 import wyraz


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

    def test_Nr01_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("ula", ["e", "x", "e"]), True)

    def test_Nr02_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("ula", ["e", "a", "x", "i", "e"]), True)

    def test_Nr03_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("kamil", ["k", "a", "m", "i", "l"]), True)

    def test_Nr04_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("zazz", ["z", "z", "z", "a"]), True)

    def test_Nr05_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("aaaz", ["a", "a", "a", "z", "z", "a"]), True)

    def test_Nr06_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("abc", ["a", "b", "c"]), True)

    def test_Nr07_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("example", ["e", "x", "a", "m", "p", "l", "e"]), True)

    def test_Nr08_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("bcbc", ["c", "c", "c", "a"]), False)

    def test_Nr11_wyraz_argumenty__(self):
        self.assertEqual(wyraz("bbbd", "cccb"), False)

    def test_Nr12_wyraz_argumenty__(self):
        self.assertEqual(wyraz("bbbd", "ccbb"), True)

    def test_Nr13_wyraz_argumenty__(self):
        self.assertEqual( wyraz("test", "hsdfkhasrwbdfskjhihwqieuqwoiruhkjxcbvmnzskf"), True)

    def test_Nr14_wyraz_argumenty__(self):
        self.assertEqual( wyraz("dluginapis", "bardzodlugistringnaprawdejestdlugi"), True)

    def test_Nr15_wyraz_argumenty__(self):
        self.assertEqual(wyraz("testowanie", "fajnytesttestujacy"), True)

    def test_Nr16_wyraz_argumenty__(self):
        self.assertEqual(wyraz("iiiiiiii", "zzzzccccvvvvviiiaaxsqweqwkjhg"), False)

    def test_Nr17_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("zzz", ["z", "a", "a", "z", "z", "a"]), True)

    def test_Nr18_wyraz_argumenty__tablica(self):
        self.assertEqual(wyraz("aaa", ["a", "a", "a", "z", "z", "a"]), True)
