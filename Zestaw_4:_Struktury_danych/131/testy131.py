import unittest
import os
import sys
import importlib

from szablon131 import dodaj, odejmij, pomnoz


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
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["123", "45"], ["678", "90"]), ("802", "35"))

    def test_Nr02_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["123", "5"], ["678", "95"]), ("802", "45"))

    def test_Nr03_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["123", "45"], ["678", "55"]), ("802", "0"))

    def test_Nr04_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["-123", "45"], ["678", "90"]), ("555", "45"))

    def test_Nr05_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["0", "0"], ["0", "0"]), ("0", "0"))

    def test_Nr06_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["2", "80"], ["2", "2"]), ("5", "0"))

    def test_Nr07_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["2", "514"], ["2", "2"]), ("4", "714"))

    def test_Nr08_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["2", "514"], ["2", "123"]), ("4", "637"))

    def test_Nr09_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["0", "514"], ["0", "6"]), ("1", "114"))

    def test_Nr10_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["-2", "22"], ["2", "24"]), ("0", "02"))

    def test_Nr11_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["-2", "22"], ["-2", "24"]), ("-4", "46"))

    def test_Nr12_dodaj_argumenty_tablica_tablica(self):
        self.assertEqual(dodaj(["0", "22"], ["-0", "24"]), ("-0", "02"))

    def test_Nr01_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["2", "514"], ["2", "2"]), ("0", "314"))

    def test_Nr02_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["2", "22"], ["2", "2"]), ("0", "02"))

    def test_Nr03_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["2", "22"], ["2", "24"]), ("-0", "02"))

    def test_Nr04_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["2", "22"], ["-2", "24"]), ("4", "46"))

    def test_Nr05_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["-0", "22"], ["-0", "24"]), ("0", "02"))

    def test_Nr06_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["0", "012"], ["0", "10"]), ("-0", "088"))

    def test_Nr07_odejmij_argumenty_tablica_tablica(self):
        self.assertEqual(odejmij(["2", "22222"], ["5", "22222"]), ("-3", "0"))

    def test_Nr01_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["0", "001"], ["-1", "0"]), ("-0", "001"))

    def test_Nr02_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["-4", "001"], ["-1", "012"]), ("4", "049012"))

    def test_Nr03_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["2", "22222"], ["5", "22222"]), ("11", "6049217284"))

    def test_Nr04_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["12", "345"], ["67", "89"]), ("838", "10205"))

    def test_Nr05_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["-12", "345"], ["67", "89"]), ("-838", "10205"))

    def test_Nr06_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["0", "0"], ["0", "0"]), ("0", "0"))

    def test_Nr07_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["12", "34"], ["-56", "78"]), ("-700", "6652"))

    def test_Nr08_pomnoz_argumenty_tablica_tablica(self):
        self.assertEqual(pomnoz(["0", "0"], ["1", "123"]), ("0", "0"))
