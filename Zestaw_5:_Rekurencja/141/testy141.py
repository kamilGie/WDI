import unittest
import os
import sys
import importlib

from szablon141 import Zadanie_141


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

    def test_Nr01_Zadanie_141_argumenty_tablica_4(self):
        self.assertEqual(Zadanie_141([1, 2, 3], 4), True)

    def test_Nr02_Zadanie_141_argumenty_tablica_10(self):
        self.assertEqual(Zadanie_141([5, 10, 15], 10), True)

    def test_Nr03_Zadanie_141_argumenty_tablica_9(self):
        self.assertEqual(Zadanie_141([4, 3, 5], 9), True)

    def test_Nr04_Zadanie_141_argumenty_tablica_7(self):
        self.assertEqual(Zadanie_141([7, 12, 15], 7), True)

    def test_Nr05_Zadanie_141_argumenty_tablica_40(self):
        self.assertEqual(Zadanie_141([10, 15, 25, 30, 35], 40), True)

    def test_Nr06_Zadanie_141_argumenty_tablica_39(self):
        self.assertEqual(Zadanie_141([10, 15, 25, 30, 35], 39), False)

    def test_Nr07_Zadanie_141_argumenty_tablica_5(self):
        self.assertEqual(Zadanie_141([1, 2, 4, 8, 16, 32], 5), True)

    def test_Nr08_Zadanie_141_argumenty_tablica_0(self):
        self.assertEqual(Zadanie_141([1, 2, 4, 8, 16, 32], 0), True)

    def test_Nr09_Zadanie_141_argumenty_tablica_11(self):
        self.assertEqual(Zadanie_141([3, 6, 9, 12], 11), False)

    def test_Nr10_Zadanie_141_argumenty_tablica_10(self):
        self.assertEqual(Zadanie_141([8, 4, 3, 7, 2], 10), True)

    def test_Nr11_Zadanie_141_argumenty_tablica_22(self):
        self.assertEqual(Zadanie_141([1, 2, 4, 8, 16, 32, 64], 22), True)

    def test_Nr12_Zadanie_141_argumenty_tablica_54(self):
        self.assertEqual(Zadanie_141([5, 10, 15, 20], 54), False)
