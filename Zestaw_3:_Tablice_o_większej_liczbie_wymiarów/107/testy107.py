import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon107 import Zadanie_107


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[23, 31, 41], [12, 15, 19], [2, 7, 3]]), False)

    def test_Nr02_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[22, 33, 44], [12, 24, 36], [5, 6, 7]]), False)

    def test_Nr03_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[2, 3, 5], [7, 11, 13], [17, 19, 23]]), True)

    def test_Nr04_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), False)

    def test_Nr05_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[5, 3, 7], [13, 5, 2], [2, 6, 9]]), True)

    def test_Nr06_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[7, 23, 29], [31, 37, 41], [53, 59, 67]]), True)

    def test_Nr07_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[15, 22, 18], [17, 23, 29], [12, 24, 36]]), False)

    def test_Nr08_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), True)

    def test_Nr09_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[22, 33, 44], [15, 17, 19], [3, 5, 7]]), False)

    def test_Nr10_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[10, 23, 17], [37, 25, 11], [13, 7, 3]]), True)

    def test_Nr11_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[22, 24, 27], [13, 19, 21], [7, 9, 5]]), False)

    def test_Nr12_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[23, 33, 11], [17, 19, 2], [7, 5, 13]]), True)

    def test_Nr13_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[3, 5, 2], [7, 11, 17], [13, 29, 23]]), True)

    def test_Nr14_Zadanie_107_argumenty_tablica(self):
            self.assertEqual(Zadanie_107([[30, 32, 35], [37, 39, 41], [43, 45, 47]]), False)


