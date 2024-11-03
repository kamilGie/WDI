import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon42 import Zadanie_42


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

    def test_Nr01_Zadanie_42_argumenty_1_1(self):
        self.assertEqual(Zadanie_42(1, 1), True)
    def test_Nr02_Zadanie_42_argumenty_123_231(self):
        self.assertEqual(Zadanie_42(123, 231), True)
    def test_Nr03_Zadanie_42_argumenty_5749_4597(self):
        self.assertEqual(Zadanie_42(5749, 4597), True)
    def test_Nr04_Zadanie_42_argumenty_123_124(self):
        self.assertEqual(Zadanie_42(123, 124), False)
    def test_Nr05_Zadanie_42_argumenty_1233_1223(self):
        self.assertEqual(Zadanie_42(1233, 1223), False)
    def test_Nr06_Zadanie_42_argumenty_987654321_123456789(self):
        self.assertEqual(Zadanie_42(987654321, 123456789), True)
    def test_Nr07_Zadanie_42_argumenty_10001_11000(self):
        self.assertEqual(Zadanie_42(10001, 11000), True)
    def test_Nr08_Zadanie_42_argumenty_12345555_55554312(self):
        self.assertEqual(Zadanie_42(12345555, 55554312), True)
    def test_Nr09_Zadanie_42_argumenty_12_21(self):
        self.assertEqual(Zadanie_42(12, 21), True)
    def test_Nr10_Zadanie_42_argumenty_999999_999999(self):
        self.assertEqual(Zadanie_42(999999, 999999), True)
    def test_Nr11_Zadanie_42_argumenty_1234567890987654321_98765432100987654321(self):
        self.assertEqual(Zadanie_42(1234567890987654321, 98765432100987654321), False)
    def test_Nr12_Zadanie_42_argumenty_1234567890987654321_1234567890123456789(self):
        self.assertEqual(Zadanie_42(1234567890987654321, 1234567890123456789), True)
    def test_Nr13_Zadanie_42_argumenty_92813781972481279368_187639812778654127983(self):
        self.assertEqual(Zadanie_42(92813781972481279368, 187639812778654127983), False)
    def test_Nr14_Zadanie_42_argumenty_217318927398127839_9712893712(self):
        self.assertEqual(Zadanie_42(217318927398127839, 9712893712), False)
    def test_Nr15_Zadanie_42_argumenty_1111111111111111111111111_1111111111111111111111111(self):
        self.assertEqual(Zadanie_42(1111111111111111111111111, 1111111111111111111111111), True)
    def test_Nr16_Zadanie_42_argumenty_11111111111111111111111111119_1111111111111111111111111111118(self):
        self.assertEqual(Zadanie_42(11111111111111111111111111119, 1111111111111111111111111111118), False)
    def test_Nr17_Zadanie_42_argumenty_2115_5112(self):
        self.assertEqual(Zadanie_42(2115, 5112), True)

