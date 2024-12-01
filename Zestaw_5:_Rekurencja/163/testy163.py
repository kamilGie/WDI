import unittest
import os
import sys
import importlib

from szablon163 import Zadanie_163


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

    def test_Nr01_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1,1),(2,2),(3,3),(4,4)] ,10 ,4), True)

    def test_Nr02_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1,1),(2,2),(3,3)] ,3 ,3), True)

    def test_Nr03_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10,10),(20,20),(30,30)],3,5), False)

    def test_Nr04_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10,10),(20,20),(30,30)] ,5,3), False)

    def test_Nr05_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1,2),(2,3),(3,4),(4,5),(5,6)], 3.5, 5), False)

    def test_Nr06_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(100, 200), (300, 400), (500, 600), (700, 800), (900, 1000)] ,1500,9), True)

    def test_Nr07_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1000, 2000), (3000, 4000), (5000, 6000), (7000, 8000)] ,5000,3), False)

    def test_Nr08_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1234, 5678), (91011, 121314), (151617, 181920), (212223, 242526)],10,2), False)

    def test_Nr09_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(i * 10, i * 10) for i in range(1, 100)],1000,99), True)

    def test_Nr10_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1, 1), (4, 4), (6, 6), (7, 7)],6,3), True)

    def test_Nr18_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(1, 1), (4, 4), (6, 6), (7, 7)],4,3), False)

    def test_Nr19_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],14,6), False)

    def test_Nr20_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],20,6), False)

    def test_Nr21_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],25,6), False)

    def test_Nr22_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],30,6), True)

    def test_Nr23_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],27,6), False)

    def test_Nr24_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],28,6), False)

    def test_Nr25_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],29,6), True)

    def test_Nr26_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],40,3), True)

    def test_Nr27_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],30,3), True)

    def test_Nr28_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],20,3), False)

    def test_Nr29_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80)],29,3), True)

    def test_Nr30_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(3, 4), (6, 8), (9, 12)],5,2), False)

    def test_Nr31_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(3, 4), (6, 8), (9, 12)],5,3), False)

    def test_Nr32_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(3, 4), (6, 8), (9, 12)],7,3), False)

    def test_Nr33_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(3, 4), (6, 8), (9, 12)],10,3), False)

    def test_Nr34_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(3, 4), (6, 8), (9, 12)],15,3), True)

    def test_Nr35_Zadanie_163(self):
            self.assertEqual(Zadanie_163([(3, 4), (6, 8), (9, 12)],15,2), False)


