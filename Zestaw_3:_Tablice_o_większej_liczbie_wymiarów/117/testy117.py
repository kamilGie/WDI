import unittest

from szablon117 import Zadanie_117


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
    import os
    import sys
    import importlib
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [1, 2, 3, 5, 8],    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0]]), 5)

    def test_Nr02_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0],    [8, 5, 3, 2, 1],    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0]]), 5)

    def test_Nr03_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0],    [0, 1, 0, 0, 0],    [0, 2, 0, 0, 0],    [0, 3, 0, 0, 0],    [0, 5, 0, 0, 0]]), 4)

    def test_Nr04_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 8, 0],    [0, 0, 0, 5, 0],    [0, 0, 0, 3, 0],    [0, 0, 0, 2, 0],    [0, 0, 0, 1, 0]]), 5)

    def test_Nr05_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0],    [3, 5, 8, 13, 21],    [0, 0, 0, 0, 0],    [0, 0, 0, 0, 0]]), 5)

    def test_Nr06_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0],    [0, 0, 3, 0, 0],    [0, 0, 5, 0, 0],    [0, 0, 8, 0, 0],    [0, 0, 13, 0, 0]]), 4)

    def test_Nr07_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 1, 2, 3, 5, 8],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0]]), 5)

    def test_Nr08_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [1, 0, 1, 2, 0, 2, 2, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [1, 1, 0, 1, 2, 3, 5, 8],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 3, 5, 0, 0, 0, 0],    [0, 0, 3, 5, 0, 0, 0, 0],    [0, 3, 5, 0, 0, 0, 0, 0]]), 5)

    def test_Nr09_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 8],    [0, 0, 0, 0, 0, 0, 0, 5],    [0, 0, 0, 0, 0, 0, 0, 3],    [0, 0, 0, 0, 0, 0, 0, 2],    [0, 0, 0, 0, 0, 0, 0, 1],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0]]), 5)

    def test_Nr10_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 3, 5, 8, 13, 21],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0]]), 5)

    def test_Nr11_Zadanie_117(self):
            self.assertEqual(Zadanie_117([    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 3, 987, 1597, 2584, 21],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 0, 0]]), 3)


