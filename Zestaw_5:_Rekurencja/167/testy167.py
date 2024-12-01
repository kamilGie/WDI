import unittest
import os
import sys
import importlib

from szablon167 import Zadanie_167


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

    def test_Nr01_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("ababa"), 4)

    def test_Nr02_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("apple"), 4)

    def test_Nr03_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("education"), 8)

    def test_Nr04_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("aeiou"), 1)

    def test_Nr05_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("aabbccddeeffg"), 7)

    def test_Nr06_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("aaeiou"), 1)

    def test_Nr07_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("bcdfghjaklmnpqrstvwaxyz"), 12)

    def test_Nr08_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("abecadlo"), 12)

    def test_Nr09_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("programming"), 9)

    def test_Nr10_Zadanie_167_argumenty_(self):
        self.assertEqual(Zadanie_167("abcdefghijklmnopqrstuvwxyz"), 576)
