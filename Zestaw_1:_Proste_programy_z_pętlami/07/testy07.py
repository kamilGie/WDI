import unittest
import os
import sys
import importlib

from szablon07 import newton_cuberoot


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


# Jak te testy daja jakies glupoty to nie moja wina taka odp daje funkcja z bitu xdd


class testy(unittest.TestCase):

    def test_Nr01_newton_cuberoot_argumenty_1(self):
        wynik = newton_cuberoot(1)

        self.assertAlmostEqual(wynik, 1.0000000000060312, places=4)

    def test_Nr02_newton_cuberoot_argumenty_2(self):
        wynik = newton_cuberoot(2)

        self.assertAlmostEqual(wynik, 1.2599210498948732, places=4)

    def test_Nr03_newton_cuberoot_argumenty_5(self):
        wynik = newton_cuberoot(5)

        self.assertAlmostEqual(wynik, 1.7099759466767002, places=4)

    def test_Nr04_newton_cuberoot_argumenty_10(self):
        wynik = newton_cuberoot(10)

        self.assertAlmostEqual(wynik, 2.1544346900338307, places=4)

    def test_Nr05_newton_cuberoot_argumenty_20(self):
        wynik = newton_cuberoot(20)

        self.assertAlmostEqual(wynik, 2.7144176166505067, places=4)

    def test_Nr06_newton_cuberoot_argumenty_39(self):
        wynik = newton_cuberoot(39)

        self.assertAlmostEqual(wynik, 3.391211443014167, places=4)

    def test_Nr07_newton_cuberoot_argumenty_50(self):
        wynik = newton_cuberoot(50)

        self.assertAlmostEqual(wynik, 3.684031498640391, places=4)

    def test_Nr08_newton_cuberoot_argumenty_100(self):
        wynik = newton_cuberoot(100)

        self.assertAlmostEqual(wynik, 4.641588833612905, places=4)

    def test_Nr09_newton_cuberoot_argumenty_8(self):
        wynik = newton_cuberoot(8)

        self.assertAlmostEqual(wynik, 2.0000000000000004, places=4)

    def test_Nr10_newton_cuberoot_argumenty_16(self):
        wynik = newton_cuberoot(16)

        self.assertAlmostEqual(wynik, 2.519842099789783, places=4)

    def test_Nr11_newton_cuberoot_argumenty_125(self):
        wynik = newton_cuberoot(125)

        self.assertAlmostEqual(wynik, 5.0, places=4)

    def test_Nr12_newton_cuberoot_argumenty_225(self):
        wynik = newton_cuberoot(225)

        self.assertAlmostEqual(wynik, 6.0822019955734, places=4)

    def test_Nr13_newton_cuberoot_argumenty_1000(self):
        wynik = newton_cuberoot(1000)

        self.assertAlmostEqual(wynik, 10.000000000000002, places=4)

    def test_Nr14_newton_cuberoot_argumenty_1410(self):
        wynik = newton_cuberoot(1410)

        self.assertAlmostEqual(wynik, 11.213461704540999, places=4)

    def test_Nr15_newton_cuberoot_argumenty_2004(self):
        wynik = newton_cuberoot(2004)

        self.assertAlmostEqual(wynik, 12.607604379179207, places=4)

    def test_Nr16_newton_cuberoot_argumenty_2115(self):
        wynik = newton_cuberoot(2115)

        self.assertAlmostEqual(wynik, 12.836209321514957, places=4)
