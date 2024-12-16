import unittest
from contextlib import redirect_stdout
import io

from szablon2024_2A import luck17


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

    def test_Nr01_luck17(self):
            self.assertEqual(luck17([        [69, 69, 69, 69, 69, 69],        [69, 1,  1,  1,  1,  69],        [69, 69, 69, 69, 1,  69],        [69, 69,  69, 69, 1,  69],        [69, 69,  69, 69, 1,  69],        [69, 1, 1, 1, 1, 69]    ]), True)

    def test_Nr02_luck17(self):
            self.assertEqual(luck17([        [2, 2, 2, 2, 2, 2],        [2, 1,  1,  1,  1,  2],        [2, 2, 2, 2, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 1, 1, 1, 1, 2]    ]), True)

    def test_Nr03_luck17(self):
            self.assertEqual(luck17([        [2, 2, 2, 2, 2, 2],        [2, 1,  1,  1,  1,  2],        [2, 2, 2, 2, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 1, 2, 1, 1, 2]    ]), True)

    def test_Nr04_luck17(self):
            self.assertEqual(luck17([        [2, 2, 2, 2, 2, 2],        [2, 1,  1,  1,  1,  2],        [2, 2, 2, 2, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 2, 2, 2, 2, 2]    ]), True)

    def test_Nr05_luck17(self):
            self.assertEqual(luck17([        [2, 2, 2, 2, 2, 2],        [2, 1,  1,  1,  1,  2],        [2, 2, 2, 3, 1,  2],        [2, 2,  5, 4, 1,  2],        [2, 2,  2, 2, 1,  2],        [2, 2, 2, 2, 2, 2]    ]), False)

    def test_Nr06_luck17(self):
            self.assertEqual(luck17([        [34, 41, 34, 34, 34, 41],        [41, 1,  1,  1,  1,  41],        [41, 41, 41, 34, 1,  34],        [41, 41,  34, 4, 1,  34],        [41, 41,  34, 34, 1,  34],        [34, 34, 34, 41, 41, 41]    ]), False)

    def test_Nr07_luck17(self):
            self.assertEqual(luck17( [    [21, 34, 21, 34, 21, 34],    [34, 1,  1,  1,  1,  21],    [21, 34, 21, 34, 1,  34],    [34, 21, 34, 21, 1,  21],    [21, 34, 21, 34, 1,  34],    [34, 1,  1,  1,  1,  21]]), True)

    def test_Nr08_luck17(self):
            self.assertEqual(luck17( [    [21, 34, 21, 34, 21, 34],    [34, 1,  1,  1,  1,  21],    [21, 34, 21, 34, 1,  34],    [34, 21, 34, 21, 1,  21],    [21, 34, 21, 34, 1,  34],    [34, 1,  21,  21,  1,  21]]), True)

    def test_Nr09_luck17(self):
            self.assertEqual(luck17( [    [21, 34, 21, 34, 21, 34],    [34, 1,  1,  1,  1,  21],    [21, 34, 21, 34, 21,  34],    [34, 21, 34, 21, 21,  21],    [21, 34, 21, 34, 1,  34],    [34, 1,  21,  21,  1,  21]]), True)

    def test_Nr10_luck17(self):
            self.assertEqual(luck17( [    [21, 34, 21, 34, 21, 34],    [34, 21,  1,  21,  1,  21],    [21, 34, 21, 34, 21,  34],    [34, 21, 34, 21, 21,  21],    [21, 34, 21, 34, 1,  34],    [34, 1,  21,  21,  1,  21]]), False)

    def test_Nr11_luck17(self):
            self.assertEqual(luck17( [    [21, 34, 21, 34, 21, 34],    [34, 21,  1,  21,  1,  21],    [21, 34, 21, 1, 21,  34],    [34, 21, 1, 21, 21,  21],    [21, 34, 21, 34, 1,  34],    [34, 1,  21,  21,  1,  21]]), False)

    def test_Nr12_luck17(self):
            self.assertEqual(luck17([    [21, 34, 21, 34, 21, 34],    [34, 21, 34, 21, 34, 21],    [21, 34, 21, 34, 21, 34],    [34, 21, 34, 21, 34, 21],    [21, 34, 21, 1,  21, 34],    [34, 21, 1,  21, 34, 21]]), True)

    def test_Nr13_luck17(self):
            self.assertEqual(luck17([[21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 21], [21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 21], [21, 34, 21, 1, 21, 34], [34, 21, 1, 21, 34, 21]]), True)

    def test_Nr14_luck17(self):
            self.assertEqual(luck17([[21, 21, 34, 21, 34, 34], [34, 21, 34, 21, 21, 34], [21, 34, 1, 34, 21, 21], [34, 21, 34, 21, 34, 34], [21, 21, 34, 1, 21, 34], [34, 21, 21, 34, 21, 21]]), True)

    def test_Nr15_luck17(self):
            self.assertEqual(luck17([[21, 34, 21, 34, 21, 21], [34, 21, 34, 21, 34, 34], [21, 21, 34, 21, 1, 21], [34, 34, 21, 34, 21, 34], [21, 21, 34, 21, 34, 21], [34, 21, 21, 34, 21, 34]]), False)

    def test_Nr16_luck17(self):
            self.assertEqual(luck17([[21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 34], [21, 21, 34, 21, 21, 21], [34, 21, 34, 1, 34, 21], [21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 1, 21]]), True)

    def test_Nr17_luck17(self):
            self.assertEqual(luck17([[34, 21, 34, 21, 34, 21], [21, 34, 21, 34, 21, 34], [34, 21, 1, 34, 21, 34], [21, 34, 34, 21, 34, 21], [34, 21, 34, 1, 21, 34], [21, 34, 21, 34, 34, 21]]), True)

    def test_Nr18_luck17(self):
            self.assertEqual(luck17([[21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 21], [21, 34, 21, 34, 21, 1], [34, 21, 34, 1, 34, 21], [21, 34, 21, 34, 21, 34], [34, 21, 1, 21, 34, 21]]), False)

    def test_Nr19_luck17(self):
            self.assertEqual(luck17([[21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 21], [21, 1, 34, 21, 34, 1], [34, 21, 34, 21, 1, 34], [21, 34, 21, 34, 21, 34], [34, 21, 1, 21, 34, 21]]), False)

    def test_Nr20_luck17(self):
            self.assertEqual(luck17([[34, 21, 34, 21, 34, 21], [21, 34, 21, 34, 21, 34], [34, 21, 1, 34, 21, 34], [21, 34, 21, 1, 34, 21], [34, 21, 34, 21, 1, 34], [21, 34, 21, 34, 21, 21]]), True)

    def test_Nr21_luck17(self):
            self.assertEqual(luck17([[21, 21, 34, 34, 21, 34], [34, 34, 21, 1, 34, 21], [21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 1], [21, 34, 21, 34, 21, 34], [34, 21, 34, 1, 21, 21]]), False)

    def test_Nr22_luck17(self):
            self.assertEqual(luck17([[21, 34, 21, 34, 21, 34], [34, 21, 34, 21, 34, 21], [21, 34, 21, 1, 34, 21], [34, 1, 34, 21, 34, 21], [21, 34, 1, 34, 21, 34], [34, 21, 34, 21, 1, 21]]), True)

    def test_Nr23_luck17(self):
            self.assertEqual(luck17([[34, 21, 34, 21, 34, 21], [21, 34, 21, 34, 21, 34], [34, 1, 21, 34, 21, 34], [21, 34, 1, 21, 34, 21], [34, 21, 34, 21, 1, 34], [21, 34, 21, 1, 34, 21]]), True)


