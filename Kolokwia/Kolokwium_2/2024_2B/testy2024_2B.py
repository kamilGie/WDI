import unittest
from contextlib import redirect_stdout
import io

from szablon2024_2B import cykl


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

    def test_Nr01_cykl(self):
            self.assertEqual(cykl(3), "BCA")

    def test_Nr02_cykl(self):
            self.assertEqual(cykl(35), "BBBA")

    def test_Nr03_cykl(self):
            self.assertEqual(cykl(45), "CABCA")

    def test_Nr04_cykl(self):
            self.assertEqual(cykl(51), "")

    def test_Nr05_cykl(self):
            self.assertEqual(cykl(60), "BAABAAAAA")

    def test_Nr06_cykl(self):
            self.assertEqual(cykl(69), "CBABAAAA")

    def test_Nr07_cykl(self):
            self.assertEqual(cykl(12), "BBCABBCA")

    def test_Nr08_cykl(self):
            self.assertEqual(cykl(1), "")

    def test_Nr09_cykl(self):
            self.assertEqual(cykl(2), "ABBAAAA")

    def test_Nr10_cykl(self):
            self.assertEqual(cykl(4), "ACAA")

    def test_Nr11_cykl(self):
            self.assertEqual(cykl(1000), "")

    def test_Nr12_cykl(self):
            self.assertEqual(cykl(2115), "")

    def test_Nr13_cykl(self):
            self.assertEqual(cykl(1410), "")

    def test_Nr14_cykl(self):
            self.assertEqual(cykl(420), "CC")


