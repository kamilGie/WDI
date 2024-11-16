import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon133 import Zadanie_133


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

    def test_Nr01_Zadanie_133_argumenty_341(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(341)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'41', '31'})  # Porównanie z użyciem set
            

    def test_Nr02_Zadanie_133_argumenty_123(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(123)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'23', '13'})  # Porównanie z użyciem set
            

    def test_Nr03_Zadanie_133_argumenty_555(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(555)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == set())  # Porównanie z użyciem set
            

    def test_Nr04_Zadanie_133_argumenty_137(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(137)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'13', '37', '17'})  # Porównanie z użyciem set
            

    def test_Nr05_Zadanie_133_argumenty_1023(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(1023)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'23', '13', '103'})  # Porównanie z użyciem set
            

    def test_Nr06_Zadanie_133_argumenty_1001(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(1001)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'101', '11'})  # Porównanie z użyciem set
            

    def test_Nr07_Zadanie_133_argumenty_987654321(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(987654321)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'9631', '9871', '87641', '75431', '764321', '98641', '8753', '8741', '853', '7643', '41', '987631', '987541', '98765431', '98543', '97651', '421', '641', '87541', '876431', '9431', '97', '6421', '8431', '8641', '96431', '8761', '521', '83', '7541', '9521', '98764321', '53', '986543', '87631', '43', '31', '941', '953', '98621', '94321', '8543', '76541', '86531', '541', '643', '975421', '9754321', '6521', '653', '8521', '71', '87643', '76543', '971', '631', '821', '97654321', '9875321', '5431', '743', '761', '9721', '7621', '863', '9643', '9743', '9421', '751', '983', '7321', '98731', '8731', '8765321', '76421', '87421', '8764321', '431', '865321', '9851', '98321', '61', '73'})  # Porównanie z użyciem set
            

    def test_Nr08_Zadanie_133_argumenty_123456789(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(123456789)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'23567', '2347', '29', '12457', '13567', '1789', '1579', '167', '17', '137', '25679', '23459', '467', '12689', '79', '239', '569', '13679', '13', '12569', '3457', '2357', '379', '269', '5689', '127', '145679', '345679', '1249', '457', '245789', '179', '1567', '13469', '2389', '34679', '257', '13457', '12479', '345689', '149', '59', '349', '13789', '1279', '12347', '19', '37', '359', '4789', '67', '23', '1489', '34589', '89', '4567', '2789', '1235789', '2459', '125789', '235679', '235789', '4679', '367', '124679', '139', '1237', '47', '2467', '124567', '347', '23789', '1456789', '3469', '3467', '157', '1259', '389', '1234789', '23456789', '1289', '12589', '1367', '1459', '479', '1245689', '123457', '23689', '12379', '134789', '234589', '123479', '2579', '2689', '12356789', '15679'})  # Porównanie z użyciem set
            

    def test_Nr09_Zadanie_133_argumenty_2025(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(2025)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == set())  # Porównanie z użyciem set
            

    def test_Nr10_Zadanie_133_argumenty_406(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(406)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == set())  # Porównanie z użyciem set
            

    def test_Nr11_Zadanie_133_argumenty_299(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(299)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'29'})  # Porównanie z użyciem set
            

    def test_Nr12_Zadanie_133_argumenty_5143(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(5143)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'43', '53', '13'})  # Porównanie z użyciem set
            

    def test_Nr13_Zadanie_133_argumenty_281(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(281)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == set())  # Porównanie z użyciem set
            

    def test_Nr14_Zadanie_133_argumenty_2115(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_133(2115)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'211', '11'})  # Porównanie z użyciem set
            


