import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon139 import Zadanie_139


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

    def test_Nr01_Zadanie_139_argumenty_10(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_139(10)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'5', '10', '1', '9', '2', '8', '4', '3', '6'})  # Porównanie z użyciem set
            

    def test_Nr02_Zadanie_139_argumenty_20(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_139(20)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'3', '12', '15', '5', '16', '10', '1', '20', '9', '2', '8', '4', '18', '6'})  # Porównanie z użyciem set
            

    def test_Nr03_Zadanie_139_argumenty_50(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_139(50)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'15', '16', '48', '40', '2', '12', '5', '10', '20', '27', '32', '3', '25', '1', '50', '9', '36', '8', '4', '18', '45', '30', '24', '6'})  # Porównanie z użyciem set
            

    def test_Nr04_Zadanie_139_argumenty_100(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_139(100)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'15', '16', '48', '96', '40', '2', '60', '80', '12', '64', '5', '10', '20', '27', '32', '3', '54', '25', '72', '1', '50', '9', '36', '8', '4', '81', '75', '18', '90', '45', '30', '24', '6', '100'})  # Porównanie z użyciem set
            

    def test_Nr05_Zadanie_139_argumenty_1000(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_139(1000)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'729', '15', '375', '648', '20', '27', '108', '250', '32', '960', '25', '810', '9', '50', '225', '36', '81', '75', '720', '486', '384', '450', '240', '150', '40', '972', '80', '675', '64', '540', '270', '135', '900', '90', '192', '576', '45', '120', '243', '24', '500', '1000', '800', '216', '16', '360', '256', '48', '96', '600', '2', '162', '400', '60', '10', '750', '3', '54', '72', '1', '320', '864', '324', '4', '18', '480', '144', '160', '30', '5', '432', '128', '625', '512', '12', '768', '200', '180', '640', '405', '300', '125', '8', '288', '6', '100'})  # Porównanie z użyciem set
            

    def test_Nr06_Zadanie_139_argumenty_12345(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_139(12345)
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {'729', '15', '2250', '375', '2560', '1296', '4500', '648', '7680', '12288', '1215', '5184', '2000', '20', '27', '6750', '108', '250', '2025', '1200', '32', '1080', '2160', '960', '9000', '25', '810', '9', '50', '225', '36', '81', '10935', '75', '720', '486', '384', '3375', '5120', '6144', '240', '450', '150', '2500', '7776', '9720', '6400', '11520', '4800', '1500', '8000', '40', '972', '7290', '11250', '1800', '80', '675', '64', '10800', '540', '270', '1875', '4050', '135', '8192', '1440', '1944', '3840', '5400', '5760', '4860', '3072', '3200', '900', '9375', '1280', '4320', '2700', '90', '192', '576', '3645', '120', '45', '2916', '243', '24', '500', '1000', '800', '216', '6075', '16', '360', '256', '1728', '48', '96', '600', '1250', '3600', '8640', '2', '1620', '6250', '162', '11664', '5000', '7500', '400', '60', '6912', '4096', '10', '1152', '10125', '750', '12000', '3', '54', '8100', '72', '9600', '1350', '1', '3000', '320', '864', '3888', '324', '4', '18', '12150', '2187', '3240', '2880', '10000', '480', '4608', '1125', '6480', '1600', '144', '160', '30', '8748', '4374', '5', '432', '128', '3750', '1536', '4000', '5625', '625', '3125', '2048', '512', '6561', '10368', '12', '768', '6000', '2304', '200', '180', '7200', '3456', '640', '2400', '2592', '405', '2430', '300', '5832', '9216', '8', '125', '1024', '1920', '1458', '288', '10240', '6', '100'})  # Porównanie z użyciem set
            


