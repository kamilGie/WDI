import unittest

from szablon2022_B3 import rook


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
    def test_Nr01_rook(self):
        self.assertEqual(rook(5, []), 2)

    def test_Nr02_rook(self):
        self.assertEqual(rook(5, [(1, 2), (0, 2), (2, 0), (3, 3)]), 3)

    def test_Nr03_rook(self):
        self.assertEqual(rook(5, [(1, 2), (0, 2), (2, 0), (3, 3)]), 3)

    def test_Nr04_rook(self):
        self.assertEqual(rook(2, [(1, 1), (2, 2)]), None)  

    def test_Nr05_rook(self):
        self.assertEqual(rook(7, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]), 2)

    def test_Nr06_rook(self):
        self.assertEqual(rook(5, [(0, 1), (0, 2), (1, 0), (2, 1), (3, 2)]), None)  

    def test_Nr07_rook(self):
        self.assertEqual(rook(5, [(0, 1), (0, 2), (1, 1), (2, 0), (3, 2)]), None)  

    def test_Nr08_rook(self):
        self.assertEqual(rook(5, [(0, 1), (1, 2), (2, 3), (3, 2), (4, 2)]), None)  

    def test_Nr09_rook(self):
        self.assertEqual(rook(5, [(0, 2), (1, 0), (1, 3), (2, 1), (3, 3)]), 5)

    def test_Nr10_rook(self):
        self.assertEqual(rook(5, [(0, 2), (1, 0), (1, 3), (2, 1), (3, 3)]), 5)

    def test_Nr11_rook(self):
        self.assertEqual(rook(7, [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2), (3, 1), (4, 0), (4, 2), (5, 1), (5, 2), (6, 1)]), None)  

    def test_Nr12_rook(self):
        self.assertEqual(rook(7, [(0, 0), (1, 1), (1, 2), (2, 0), (2, 2), (3, 0), (4, 1), (4, 2), (5, 0), (5, 1), (6, 1), (6, 2)]), None)  

    def test_Nr13_rook(self):
        self.assertEqual(rook(7, [(0, 1), (0, 3), (1, 0), (1, 1), (2, 0), (3, 2), (4, 0), (5, 3), (6, 2), (6, 3)]), None)  

    def test_Nr14_rook(self):
        self.assertEqual(rook(7, [(1, 1), (1, 2), (2, 0), (3, 0), (4, 1), (4, 2), (5, 0), (5, 1), (6, 1), (6, 2)]), 2)

    def test_Nr15_rook(self):
        self.assertEqual(rook(7, [(1, 1), (1, 2), (2, 0), (3, 0), (4, 1), (4, 2), (5, 0), (3, 3), (3, 4), (3, 5), (3, 6), (5, 1), (6, 1), (6, 2)]), None)  

    def test_Nr16_rook(self):
        self.assertEqual(rook(7, [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 1), (2, 4), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 6), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4)]), 11)

    def test_Nr17_rook(self):
        self.assertEqual(rook(7, [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (3, 2), (4, 0), (4, 1), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2), (5, 5), (6, 0), (6, 1), (6, 2), (6, 3)]), None)  

    def test_Nr18_rook(self):
        self.assertEqual(rook(7, [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (4, 0), (4, 1), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2), (5, 5), (6, 0), (6, 1), (6, 2), (6, 3)]), 4)
