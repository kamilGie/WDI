import unittest
from contextlib import redirect_stdout
import io

from szablon171 import hanoi_stos, hanoi_wikipedia


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

    def test_Nr01_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(1)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "a -> c")

    def test_Nr02_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(2)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "a -> b\na -> c\nb -> c")

    def test_Nr03_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(3)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik, "a -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c"
        )

    def test_Nr04_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(4)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c",
        )

    def test_Nr05_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(5)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c",
        )

    def test_Nr06_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(6)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c",
        )

    def test_Nr07_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(7)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c",
        )

    def test_Nr08_hanoi_stos(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_stos(8)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c",
        )

    def test_Nr01_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(1)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "a -> c")

    def test_Nr02_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(2)
        wynik = f.getvalue().strip()

        self.assertEqual(wynik, "a -> b\na -> c\nb -> c")

    def test_Nr03_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(3)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik, "a -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c"
        )

    def test_Nr04_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(4)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c",
        )

    def test_Nr05_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(5)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c",
        )

    def test_Nr06_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(6)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c",
        )

    def test_Nr07_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(7)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\na -> b\nc -> b\nc -> a\nb -> a\nc -> b\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c\nb -> a\nc -> b\nc -> a\nb -> a\nb -> c\na -> c\na -> b\nc -> b\na -> c\nb -> a\nb -> c\na -> c",
        )

    def test_Nr08_hanoi_wikipedia(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hanoi_wikipedia(8)
        wynik = f.getvalue().strip()

        self.assertEqual(
            wynik,
            "a -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nc -> b\na -> b\nc -> a\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c\na -> b\nc -> a\nc -> b\na -> b\na -> c\nb -> c\nb -> a\nc -> a\nb -> c\na -> b\na -> c\nb -> c",
        )
