import unittest
import os
import sys
import importlib

from szablon097 import Zadanie_97


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

    def test_Nr01_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def test_Nr02_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[1, 2, 3], [2, 3, 4], [4, 5, 6]]), [1, 5, 6, 0, 0, 0, 0, 0, 0]
        )

    def test_Nr03_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), [0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    def test_Nr04_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(Zadanie_97([[1]]), [1])

    def test_Nr05_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[1, 2, 5], [3, 4, 6], [5, 6, 7]]), [1, 2, 3, 4, 7, 0, 0, 0, 0]
        )

    def test_Nr06_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[100, 200, 300], [1000, 2000, 3000], [4000, 5000, 6000]]),
            [100, 200, 300, 1000, 2000, 3000, 4000, 5000, 6000],
        )

    def test_Nr07_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[1, 3, 5], [2, 4, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def test_Nr08_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(
            Zadanie_97([[1000000, 999999999], [1, 2]]), [1, 2, 1000000, 999999999]
        )

    def test_Nr09_Zadanie_97_argumenty_tablica(self):
        self.assertEqual(Zadanie_97([[2115]]), [2115])
