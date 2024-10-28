import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon11 import divisors


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2).run(suite)


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
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr1_divisors_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(1)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'1'})  # Porównanie z użyciem set
        
    def test_Nr2_divisors_argumenty_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(4)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'4', '1', '2'})  # Porównanie z użyciem set
        
    def test_Nr3_divisors_argumenty_36(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(36)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'36', '12', '2', '6', '3', '4', '1', '18', '9'})  # Porównanie z użyciem set
        
    def test_Nr4_divisors_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(100)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'2', '100', '20', '50', '4', '1', '10', '25', '5'})  # Porównanie z użyciem set
        
    def test_Nr5_divisors_argumenty_12345(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(12345)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'4115', '12345', '2469', '3', '823', '1', '15', '5'})  # Porównanie z użyciem set
        
    def test_Nr6_divisors_argumenty_1233(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(1233)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'411', '137', '3', '1', '9', '1233'})  # Porównanie z użyciem set
        
    def test_Nr7_divisors_argumenty_435234(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(435234)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'217617', '34', '502', '289', '72539', '1506', '102', '578', '12801', '753', '1', '251', '4267', '2', '17', '3', '25602', '435234', '867', '1734', '6', '51', '145078', '8534'})  # Porównanie z użyciem set
        
    def test_Nr8_divisors_argumenty_234123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(234123)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'1', '3', '234123', '78041'})  # Porównanie z użyciem set
        
    def test_Nr9_divisors_argumenty_54352(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(54352)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'6794', '54352', '316', '1', '632', '3397', '43', '86', '172', '2', '79', '4', '13588', '27176', '16', '344', '1264', '158', '8', '688'})  # Porównanie z użyciem set
        
    def test_Nr10_divisors_argumenty_360(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(360)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'15', '36', '12', '180', '1', '90', '40', '30', '60', '9', '2', '120', '3', '20', '4', '10', '5', '18', '72', '6', '360', '24', '8', '45'})  # Porównanie z użyciem set
        
    def test_Nr11_divisors_argumenty_3600000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(3600000)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'300000', '2250', '1200000', '15', '1800000', '1440', '48', '12500', '11250', '120000', '1', '480', '400000', '40', '6250', '64', '72000', '128', '2880', '3200', '1875', '900000', '100', '120', '576', '3', '320', '150000', '4', '60000', '1920', '5', '25000', '7500', '3000', '112500', '72', '96', '16', '14400', '450000', '625', '90000', '5625', '8', '45', '750', '1200', '1500', '4800', '960', '15000', '80', '12', '180', '30', '240000', '2400', '144000', '9375', '450', '20', '10000', '36000', '300', '3750', '150', '3600000', '12000', '48000', '3600', '32', '360', '200', '2500', '2000', '500', '9000', '9600', '28800', '144', '192', '50', '225', '80000', '3125', '20000', '37500', '400', '75000', '25', '240', '5000', '288', '1600', '30000', '225000', '1250', '1800', '6000', '10', '180000', '384', '600000', '125', '720000', '160', '5760', '100000', '18000', '56250', '22500', '1125', '18750', '640', '250', '40000', '1000', '36', '45000', '900', '75', '4500', '90', '60', '9', '2', '360000', '4000', '24000', '7200', '18', '1152', '720', '28125', '6', '800', '375', '200000', '600', '50000', '24', '8000', '16000'})  # Porównanie z użyciem set
        
    def test_Nr12_divisors_argumenty_3242346432(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(3242346432)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'624', '7176', '70485792', '736', '14352', '552', '2392', '5873816', '48', '20784272', '368', '1', '416', '64', '4416', '312', '1080782144', '3588', '16887221', '19136', '1807328', '4784', '3', '897', '4', '169437', '101323326', '2202681', '96', '677748', '16', '734227', '8', '2598034', '83137088', '202646652', '810586608', '2208', '1794', '540391072', '138', '1621173216', '23495264', '28704', '12', '1196', '208', '1248', '338874', '39', '1472', '9568', '3242346432', '1355496', '35242896', '32', '15588204', '192', '11747632', '31176408', '104', '1104', '225916', '3897051', '46990528', '10392136', '276', '8810724', '140971584', '5196068', '50661663', '3614656', '2496', '1299017', '270195536', '7794102', '92', '405293304', '112958', '598', '57408', '78', '2710992', '52', '903664', '23', '135097768', '184', '2936908', '156', '46', '249411264', '26', '41568544', '5421984', '832', '451832', '62352816', '2', '33774442', '56479', '17621448', '67548884', '299', '10843968', '13', '124705632', '4405362', '6', '24', '1468454', '69'})  # Porównanie z użyciem set
        
    def test_Nr13_divisors_argumenty_104729(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(104729)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'1', '104729'})  # Porównanie z użyciem set
        
    def test_Nr14_divisors_argumenty_102523(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(102523)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'1', '102523'})  # Porównanie z użyciem set
        
    def test_Nr15_divisors_argumenty_101527(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(101527)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'1', '101527'})  # Porównanie z użyciem set
        
    def test_Nr16_divisors_argumenty_234234(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(234234)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'182', '3003', '22', '6006', '1014', '16731', '26', '21', '63', '39039', '143', '169', '1521', '9009', '13013', '234234', '429', '11154', '3042', '198', '10647', '2002', '819', '338', '1', '126', '1638', '286', '462', '7098', '507', '546', '66', '9', '39', '5577', '1386', '231', '693', '2', '91', '234', '1001', '3', '3718', '42', '1287', '2574', '117117', '273', '7', '18', '13', '26026', '117', '14', '18018', '78', '1859', '33462', '78078', '154', '6', '1183', '3549', '2366', '99', '11', '21294', '33', '77', '858'})  # Porównanie z użyciem set
        
    def test_Nr17_divisors_argumenty_234234(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(234234)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'182', '3003', '22', '6006', '1014', '16731', '26', '21', '63', '39039', '143', '169', '1521', '9009', '13013', '234234', '429', '11154', '3042', '198', '10647', '2002', '819', '338', '1', '126', '1638', '286', '462', '7098', '507', '546', '66', '9', '39', '5577', '1386', '231', '693', '2', '91', '234', '1001', '3', '3718', '42', '1287', '2574', '117117', '273', '7', '18', '13', '26026', '117', '14', '18018', '78', '1859', '33462', '78078', '154', '6', '1183', '3549', '2366', '99', '11', '21294', '33', '77', '858'})  # Porównanie z użyciem set
        
    def test_Nr18_divisors_argumenty_2398468234(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(2398468234)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'92146', '2', '52058', '26029', '46073', '1', '2398468234', '1199234117'})  # Porównanie z użyciem set
        
    def test_Nr19_divisors_argumenty_1234(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(1234)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'1', '2', '617', '1234'})  # Porównanie z użyciem set
        
    def test_Nr20_divisors_argumenty_1410(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(1410)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'47', '1410', '2', '6', '235', '3', '470', '30', '94', '1', '705', '282', '5', '10', '141', '15'})  # Porównanie z użyciem set
        
    def test_Nr21_divisors_argumenty_2115(self):
        f = io.StringIO()
        with redirect_stdout(f):
            divisors(2115)
        wynik = f.getvalue().strip()

        # Podziel wynik na elementy i utwórz zbiór
        self.assertTrue(set(wynik.split()) == {'47', '235', '3', '423', '1', '705', '15', '5', '141', '2115', '45', '9'})  # Porównanie z użyciem set
        

