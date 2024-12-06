import unittest
from contextlib import redirect_stdout
import io

from szablon2022_A3 import king


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

    def test_Nr01_king(self):
            self.assertEqual(king(3,[]), 8)

    def test_Nr02_king(self):
            f = io.StringIO()
            with redirect_stdout(f):
                king(3,[(1, 1)])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '')

    def test_Nr03_king(self):
            self.assertEqual(king(5, []), 24)

    def test_Nr04_king(self):
            f = io.StringIO()
            with redirect_stdout(f):
                king(4,[(2, 1), (1, 2)])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '')

    def test_Nr05_king(self):
            self.assertEqual(king(4,[(3, 0), (2, 0)]), 6)

    def test_Nr06_king(self):
            f = io.StringIO()
            with redirect_stdout(f):
                king(5,[(0, 1), (1, 0), (4, 3), (3, 4)])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '')

    def test_Nr07_king(self):
            f = io.StringIO()
            with redirect_stdout(f):
                king(5,[(0, 1), (4, 3), (3, 4)])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '')

    def test_Nr08_king(self):
            self.assertEqual(king(5,[(1, 2), (2, 2), (3, 2)]), 10)

    def test_Nr09_king(self):
            self.assertEqual(king(5,[(1, 2), (0, 4), (3, 4)]), 12)

    def test_Nr10_king(self):
            self.assertEqual(king(5,[(1, 2), (4, 0), (3, 4)]), 8)

    def test_Nr11_king(self):
            self.assertEqual(king(10,[(3, 4), (7, 8), (1, 9)]), 60)

    def test_Nr12_king(self):
            self.assertEqual(king(8,[(1, 2), (2, 4), (1, 7), (3, 6), (4, 1), (4, 6), (7,2)]), 20)

    def test_Nr13_king(self):
            self.assertEqual(king(8,[(1, 2), (2, 4), (1, 7), (3, 6), (4, 1), (4, 6), (7,2),(6,6)]), 14)

    def test_Nr14_king(self):
            f = io.StringIO()
            with redirect_stdout(f):
                king(8,[(0, 1),(1, 0),(1, 2), (2, 4), (1, 7), (3, 6), (4, 1), (4, 6), (7,2),(6,6)])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '')

    def test_Nr15_king(self):
            f = io.StringIO()
            with redirect_stdout(f):
                king(8,[(1, 2), (2, 4), (1, 7), (3, 6), (4, 1), (4, 6), (7,2),(6,6),(2, 1)])
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '')


