import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon24 import Zadanie_24


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

    def test_Nr01_Zadanie_24_argumenty_0(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(0)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = set()
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr02_Zadanie_24_argumenty_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(1)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = set()
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr03_Zadanie_24_argumenty_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(3)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"2"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr04_Zadanie_24_argumenty_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(5)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"3", "2"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr05_Zadanie_24_argumenty_10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(10)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"3", "2", "7"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr06_Zadanie_24_argumenty_20(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(20)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"3", "2", "7", "11"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr07_Zadanie_24_argumenty_50(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(50)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"3", "2", "7", "11"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr08_Zadanie_24_argumenty_100(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(100)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"3", "2", "7", "11"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr09_Zadanie_24_argumenty_121(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(121)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"3", "2", "7", "11"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr10_Zadanie_24_argumenty_150(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(150)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"11", "3", "7", "131", "121", "2"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr11_Zadanie_24_argumenty_200(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(200)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"11", "3", "7", "131", "121", "2"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr12_Zadanie_24_argumenty_400(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(400)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {"11", "323", "3", "7", "131", "121", "373", "2"}
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr13_Zadanie_24_argumenty_900(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(900)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "11",
            "323",
            "3",
            "7",
            "131",
            "121",
            "373",
            "727",
            "2",
            "737",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr14_Zadanie_24_argumenty_1000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(1000)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "979",
            "11",
            "323",
            "929",
            "3",
            "7",
            "131",
            "121",
            "373",
            "727",
            "2",
            "737",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr15_Zadanie_24_argumenty_1000000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(1000000)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "979",
            "311113",
            "323",
            "73237",
            "373",
            "121",
            "77377",
            "17371",
            "97379",
            "13231",
            "3",
            "331133",
            "33233",
            "39293",
            "7",
            "131",
            "737",
            "7117",
            "31313",
            "731137",
            "971179",
            "71317",
            "929",
            "11311",
            "93239",
            "931139",
            "1111",
            "991199",
            "37273",
            "79297",
            "93739",
            "11",
            "3113",
            "19291",
            "91319",
            "727",
            "2",
            "9119",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr16_Zadanie_24_argumenty_1000000000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(1000000000)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "991737199",
            "39911993",
            "919323919",
            "77377",
            "17371",
            "331133",
            "3332333",
            "31313",
            "93239",
            "1111",
            "937737739",
            "9392939",
            "9372739",
            "727",
            "9119",
            "3173713",
            "93111139",
            "311113",
            "73237",
            "9173719",
            "373",
            "121",
            "1973791",
            "319737913",
            "33233",
            "7",
            "1932391",
            "9932399",
            "737",
            "3732373",
            "3913193",
            "11311",
            "997737799",
            "991199",
            "3792973",
            "37273",
            "199323991",
            "793929397",
            "79297",
            "11",
            "3113",
            "9913199",
            "3132313",
            "9773779",
            "319323913",
            "19291",
            "3392933",
            "2",
            "979",
            "337323733",
            "3773773",
            "939131939",
            "7392937",
            "73311337",
            "919737919",
            "397737793",
            "13231",
            "913929319",
            "3",
            "39293",
            "7117",
            "731137",
            "971179",
            "71317",
            "733929337",
            "9732379",
            "999131999",
            "79911997",
            "931323139",
            "799323997",
            "333929333",
            "323",
            "1392931",
            "97379",
            "393323393",
            "9192919",
            "7913197",
            "799131997",
            "373929373",
            "131",
            "929",
            "399323993",
            "313929313",
            "931139",
            "139131931",
            "9332339",
            "93739",
            "997323799",
            "91319",
            "1313131",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr17_Zadanie_24_argumenty_100000000000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(100000000000)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "991737199",
            "39911993",
            "99977377999",
            "919323919",
            "77377",
            "17371",
            "331133",
            "3332333",
            "31313",
            "19391319391",
            "99139293199",
            "93239",
            "1111",
            "937737739",
            "9392939",
            "73933233937",
            "9372739",
            "727",
            "9119",
            "3173713",
            "93111139",
            "311113",
            "73237",
            "9173719",
            "373",
            "121",
            "1973791",
            "319737913",
            "33233",
            "7",
            "1932391",
            "9932399",
            "737",
            "3732373",
            "3913193",
            "3733113373",
            "11311",
            "997737799",
            "991199",
            "3792973",
            "73993239937",
            "199323991",
            "37273",
            "793929397",
            "79297",
            "11",
            "3113",
            "9913199",
            "3132313",
            "9773779",
            "319323913",
            "19291",
            "3392933",
            "2",
            "33339293333",
            "979",
            "337323733",
            "3773773",
            "939131939",
            "7392937",
            "73311337",
            "919737919",
            "33193239133",
            "397737793",
            "13231",
            "913929319",
            "3",
            "39293",
            "99313231399",
            "93933233939",
            "7117",
            "99917371999",
            "731137",
            "971179",
            "71317",
            "733929337",
            "9732379",
            "999131999",
            "33977377933",
            "79911997",
            "931323139",
            "97993239979",
            "99197379199",
            "39313231393",
            "799323997",
            "3399119933",
            "333929333",
            "39193239193",
            "323",
            "33139293133",
            "1392931",
            "97339293379",
            "97379",
            "393323393",
            "9192919",
            "7913197",
            "799131997",
            "373929373",
            "131",
            "929",
            "399323993",
            "313929313",
            "931139",
            "91391319319",
            "139131931",
            "9332339",
            "93739",
            "997323799",
            "91319",
            "1313131",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr18_Zadanie_24_argumenty_100000000000000000000(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(100000000000000000000)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "991737199",
            "39911993",
            "99977377999",
            "919323919",
            "77377",
            "17371",
            "3339999173719999333",
            "331133",
            "3332333",
            "31313",
            "19391319391",
            "99139293199",
            "93239",
            "1111",
            "3999773779993",
            "937737739",
            "9392939",
            "9999173719999",
            "73933233937",
            "9372739",
            "3391932391933",
            "727",
            "9119",
            "3173713",
            "93111139",
            "311113",
            "73237",
            "9173719",
            "3331392931333",
            "373",
            "121",
            "1973791",
            "319737913",
            "33233",
            "7",
            "1932391",
            "9932399",
            "937393323393739",
            "3732373",
            "3913193",
            "737",
            "3733113373",
            "11311",
            "3393132313933",
            "997737799",
            "991199",
            "3792973",
            "73993239937",
            "199323991",
            "37273",
            "793929397",
            "9339773779339",
            "79297",
            "11",
            "3113",
            "9913199",
            "3132313",
            "9773779",
            "319323913",
            "19291",
            "9333392933339",
            "3392933",
            "399991737199993",
            "1939332339391",
            "2",
            "33339293333",
            "979",
            "337323733",
            "3773773",
            "333919323919333",
            "939131939",
            "7392937",
            "73311337",
            "919737919",
            "33193239133",
            "397737793",
            "13231",
            "913929319",
            "3",
            "39293",
            "99313231399",
            "3739332339373",
            "93933233939",
            "7117",
            "99917371999",
            "731137",
            "971179",
            "71317",
            "733929337",
            "9732379",
            "999131999",
            "33977377933",
            "79911997",
            "931323139",
            "97993239979",
            "99197379199",
            "39313231393",
            "799323997",
            "33999917371999933",
            "3399119933",
            "333929333",
            "39193239193",
            "323",
            "33139293133",
            "1392931",
            "97339293379",
            "97379",
            "393323393",
            "9192919",
            "7913197",
            "799131997",
            "373929373",
            "131",
            "929",
            "399323993",
            "313929313",
            "9993132313999",
            "931139",
            "91391319319",
            "139131931",
            "9332339",
            "93739",
            "997323799",
            "91319",
            "1313131",
            "3991973791993",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set

    def test_Nr19_Zadanie_24_argumenty_172398126873219878123(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_24(172398126873219878123)
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "991737199",
            "39911993",
            "99977377999",
            "919323919",
            "77377",
            "17371",
            "3339999173719999333",
            "331133",
            "3332333",
            "31313",
            "19391319391",
            "99139293199",
            "93239",
            "1111",
            "3999773779993",
            "937737739",
            "9392939",
            "9999173719999",
            "73933233937",
            "9372739",
            "3391932391933",
            "727",
            "9119",
            "3173713",
            "93111139",
            "311113",
            "73237",
            "9173719",
            "3331392931333",
            "373",
            "121",
            "1973791",
            "319737913",
            "33233",
            "7",
            "1932391",
            "9932399",
            "937393323393739",
            "3732373",
            "3913193",
            "737",
            "3733113373",
            "11311",
            "3393132313933",
            "997737799",
            "991199",
            "3792973",
            "73993239937",
            "199323991",
            "37273",
            "793929397",
            "9339773779339",
            "79297",
            "11",
            "3113",
            "9913199",
            "3132313",
            "9773779",
            "319323913",
            "19291",
            "9333392933339",
            "3392933",
            "399991737199993",
            "1939332339391",
            "2",
            "33339293333",
            "979",
            "337323733",
            "3773773",
            "333919323919333",
            "939131939",
            "7392937",
            "73311337",
            "919737919",
            "33193239133",
            "397737793",
            "13231",
            "913929319",
            "3",
            "39293",
            "99313231399",
            "3739332339373",
            "93933233939",
            "7117",
            "99917371999",
            "731137",
            "971179",
            "71317",
            "733929337",
            "9732379",
            "999131999",
            "33977377933",
            "79911997",
            "931323139",
            "97993239979",
            "99197379199",
            "39313231393",
            "799323997",
            "33999917371999933",
            "3399119933",
            "333929333",
            "39193239193",
            "323",
            "33139293133",
            "1392931",
            "97339293379",
            "97379",
            "393323393",
            "9192919",
            "7913197",
            "799131997",
            "373929373",
            "131",
            "929",
            "399323993",
            "313929313",
            "9993132313999",
            "931139",
            "91391319319",
            "139131931",
            "9332339",
            "93739",
            "997323799",
            "91319",
            "1313131",
            "3991973791993",
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set
