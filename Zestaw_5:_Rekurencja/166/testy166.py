import unittest
import os
import sys
import importlib

from szablon166 import Zadanie_166


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

    def test_Nr01_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual( Zadanie_166(["ab", "cde", "cfed", "fab"], ["abc", "abc", "def", "fed"]), "abcdefabcfed",)

    def test_Nr02_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual( Zadanie_166(["abc", "defghijk"], ["abcdefg", "h", "i", "jk"]), "abcdefghijk",)

    def test_Nr03_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["ab", "abc"], ["ab", "abc"]), False)

    def test_Nr04_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["ab", "c", "def"], ["gh", "ij", "kl"]), False)

    def test_Nr05_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual( Zadanie_166(["start", "middle", "end"], ["startmi", "dd", "leend"]), "startmiddleend",)

    def test_Nr06_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["abc", "de", "fg"], ["abcd", "ef", "gh"]), False)

    def test_Nr07_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["a", "b", "c"], ["a", "b", "c"]), False)

    def test_Nr08_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["a", "b", "c"], ["a", "b"]), False)

    def test_Nr09_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["aa", "aa"], ["aaa"]), False)

    def test_Nr10_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["a", "a", "b"], ["ab", "a"]), False)

    def test_Nr11_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual(Zadanie_166(["ab", "ab", "cd"], ["ab", "cd", "cd"]), False)

    def test_Nr12_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual( Zadanie_166(["abcd", "efghij", "klmn"], ["abcdefghij", "klmn"]), False)

    def test_Nr13_Zadanie_166_argumenty_tablica_tablica(self):
        self.assertEqual( Zadanie_166(["abc","deca","bcwel"], ["ab","cwel","cde","cab"]), "abcdecabcwel",)
