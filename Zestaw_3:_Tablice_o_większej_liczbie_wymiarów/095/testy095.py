import unittest
import os
import sys
import importlib

from szablon095 import ratio_check_in_tab


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

    def test_Nr01_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(ratio_check_in_tab([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3.0)

    def test_Nr02_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(
            ratio_check_in_tab([[3, 2, 1], [1, 1, 1], [1, 1, 1]]), 1.6666666666666667
        )

    def test_Nr03_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(ratio_check_in_tab([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 1.0)

    def test_Nr04_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(
            ratio_check_in_tab([[10, 20, 30], [5, 10, 15], [2, 4, 6]]), 4.25
        )

    def test_Nr05_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(ratio_check_in_tab([[8, 2, 6], [3, 15, 3], [5, 1, 2]]), 2.25)

    def test_Nr06_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(ratio_check_in_tab([[0, 0, 1], [2, 1, 0], [4, 5, 0]]), 6.0)

    def test_Nr07_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(
            ratio_check_in_tab(
                [[100, 200, 300], [500, 1000, 1500], [2000, 4000, 6000]]
            ),
            13.0,
        )

    def test_Nr08_ratio_check_in_tab_argumenty_tablica(self):
        self.assertEqual(
            ratio_check_in_tab([[7, 14, 21], [30, 60, 90], [2, 4, 6]]), 9.75
        )
