import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon154 import Zadanie_154


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

    def test_Nr01_Zadanie_154_argumenty_tablica_15(self):
            self.assertEqual(Zadanie_154([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 7, 8, 9, 10, 11], [5, 6, 7, 8, 9, 10, 11, 12], [6, 7, 8, 9, 10, 11, 12, 13], [7, 8, 9, 10, 11, 12, 13, 14], [8, 9, 10, 11, 12, 13, 14, 15]], 15), True)

    def test_Nr02_Zadanie_154_argumenty_tablica_22(self):
            self.assertEqual(Zadanie_154([[10, 15, 3, 7, 9, 11, 13, 5], [12, 3, 5, 1, 2, 7, 6, 9], [8, 4, 3, 6, 2, 5, 1, 7], [5, 2, 9, 4, 8, 7, 6, 1], [3, 6, 4, 5, 7, 8, 9, 10], [7, 1, 2, 6, 9, 3, 5, 8], [9, 5, 7, 1, 4, 3, 8, 2], [6, 7, 9, 5, 3, 8, 2, 10]], 22), True)

    def test_Nr03_Zadanie_154_argumenty_tablica_10(self):
            self.assertEqual(Zadanie_154([[10]], 10), True)

    def test_Nr04_Zadanie_154_argumenty_tablica_1000(self):
            self.assertEqual(Zadanie_154([[100, 200, 300, 400, 500, 600, 700, 800], [90, 180, 270, 360, 450, 540, 630, 720], [80, 160, 240, 320, 400, 480, 560, 640], [70, 140, 210, 280, 350, 420, 490, 560], [60, 120, 180, 240, 300, 360, 420, 480], [50, 100, 150, 200, 250, 300, 350, 400], [40, 80, 120, 160, 200, 240, 280, 320], [30, 60, 90, 120, 150, 180, 210, 240]], 1000), True)


