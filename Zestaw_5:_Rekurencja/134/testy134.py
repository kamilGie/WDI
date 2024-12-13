import unittest

from szablon134 import Zadanie_134


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

    def test_Nr01_Zadanie_134(self):
            self.assertEqual(Zadanie_134([30, 6, 64, 2]), False)

    def test_Nr02_Zadanie_134(self):
            self.assertEqual(Zadanie_134([1, 1, 1]), True)

    def test_Nr03_Zadanie_134(self):
            self.assertEqual(Zadanie_134([30, 30, 30]), True)

    def test_Nr04_Zadanie_134(self):
            self.assertEqual(Zadanie_134([2, 3, 5, 7,11,13]), True)

    def test_Nr05_Zadanie_134(self):
            self.assertEqual(Zadanie_134([64, 128, 256]), True)

    def test_Nr06_Zadanie_134(self):
            self.assertEqual(Zadanie_134([30, 42, 66]), True)

    def test_Nr07_Zadanie_134(self):
            self.assertEqual(Zadanie_134([30, 42, 66,12]), False)

    def test_Nr08_Zadanie_134(self):
            self.assertEqual(Zadanie_134([6, 6, 6, 6]), False)

    def test_Nr09_Zadanie_134(self):
            self.assertEqual(Zadanie_134([15, 21, 35, 70]), True)

    def test_Nr10_Zadanie_134(self):
            self.assertEqual(Zadanie_134([50, 75, 100, 125]), False)

    def test_Nr11_Zadanie_134(self):
            self.assertEqual(Zadanie_134([9, 27, 81, 243]), False)

    def test_Nr12_Zadanie_134(self):
            self.assertEqual(Zadanie_134([9, 27, 81, 243]), False)

    def test_Nr13_Zadanie_134(self):
            self.assertEqual(Zadanie_134([2, 4, 8, 16, 32, 64]), True)


