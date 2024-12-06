import unittest

from szablon2022_B4 import move


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

    def test_Nr01_move(self):
            self.assertEqual(move([    [True, True, False],    [False, True, False],    [False, False, False]]), ((0, 0), (2, 0)))

    def test_Nr02_move(self):
            self.assertEqual(move([    [True, True, False],    [False, False, False],    [False, True, False]]), ((0, 0), (1, 0)))

    def test_Nr03_move(self):
            self.assertEqual(move([    [True, False, False, True],    [False, False, False, False],    [False, False, True, False],    [True, False, False, False]]), ((0, 0), (0, 1)))

    def test_Nr04_move(self):
            self.assertEqual(move([    [True, False, False],    [True, True, False],    [False, False, False]]), ((0, 0), (0, 2)))

    def test_Nr05_move(self):
            self.assertEqual(move([    [True, False, False, True],    [False, False, False, False],    [False, False, False, True],    [False, True, False, False]]), ((0, 0), (1, 0)))

    def test_Nr06_move(self):
            self.assertEqual(move([    [True, False, False, False],    [True, True, False, False],    [False, False, False, False],    [False, False, False, True]]), ((0, 0), (0, 2)))

    def test_Nr07_move(self):
            self.assertEqual(move([    [True, False, False, False, False, False, False, False],    [False, False, False, False, False, False, False, False],    [False, False, False, False, False, False, False, False],    [False, False, False, False, True, False, False, False],    [False, False, False, False, False, False, False, False],    [False, False, False, False, False, False, False, False],    [False, False, False, False, False, False, False, False],    [True, True, True, False, True, True, True, True]]), ((0, 0), (0, 3)))


