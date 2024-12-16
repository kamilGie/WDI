import unittest
from szablon2023_2B import cycle


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
    import os
    import sys
    import importlib

    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_cycle(self):
        self.assertEqual(cycle(29, 6), 5)

    def test_Nr02_cycle(self):
        self.assertEqual(cycle(31, 6), 0)

    def test_Nr04_cycle(self):
        self.assertIn(cycle(39, 8), [8, 7])

    def test_Nr05_cycle(self):
        self.assertEqual(cycle(39, 6), 6)

    def test_Nr17_cycle(self):
        self.assertEqual(cycle(39, 5), 0)

    def test_Nr12_cycle(self):
        self.assertEqual(cycle(25, 5), 0)

    def test_Nr15_cycle(self):
        self.assertEqual(cycle(25, 6), 6)

    def test_Nr07_cycle(self):
        self.assertEqual(cycle(17, 3), 0)

    def test_Nr21_cycle(self):
        self.assertEqual(cycle(17, 4), 4)
