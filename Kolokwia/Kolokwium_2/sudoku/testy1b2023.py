import unittest
import os
import sys
import importlib

from szablon1b2023 import sudoku


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
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr18_sudoku_argumenty_tablica(self):
        wynik = sudoku(
            [
                [8, 1, 2, 7, 5, 3, 6, 4, 9],
                [9, 4, 3, 6, 8, 2, 1, 7, 5],
                [6, 7, 5, 4, 9, 1, 2, 8, 3],
                [1, 5, 4, 3, 6, 8, 8, 9, 6],
                [3, 6, 9, 9, 1, 7, 7, 2, 1],
                [2, 8, 7, 4, 5, 2, 5, 3, 4],
                [5, 2, 1, 9, 7, 4, 2, 3, 7],
                [4, 3, 8, 5, 2, 6, 8, 4, 5],
                [7, 9, 6, 3, 1, 8, 1, 6, 9],
            ]
        )

        oczekiwany_wynik = [(5, 9)]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr20_sudoku_argumenty_tablica(self):
        wynik = sudoku(
            [
                [6, 7, 8, 5, 3, 4, 9, 1, 2],
                [1, 9, 5, 6, 7, 2, 3, 4, 8],
                [3, 4, 2, 1, 9, 8, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]
        )

        oczekiwany_wynik = [(1, 4)]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr26_sudoku_argumenty_tablica(self):
        wynik = sudoku(
            [
                [5, 3, 4, 6, 7, 8, 7, 6, 1],
                [6, 7, 2, 1, 9, 5, 8, 5, 3],
                [1, 9, 8, 3, 4, 2, 9, 2, 4],
                [8, 5, 9, 9, 1, 2, 4, 2, 3],
                [4, 2, 6, 3, 4, 8, 7, 9, 1],
                [7, 1, 3, 5, 6, 7, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]
        )

        oczekiwany_wynik = [(5, 7)]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr31_sudoku_argumenty_tablica(self):
        wynik = sudoku(
            [
                [9, 1, 2, 4, 5, 6, 7, 8, 9],
                [3, 4, 5, 7, 8, 9, 1, 2, 3],
                [6, 7, 8, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 1, 2, 3],
                [6, 7, 8, 9, 1, 2, 4, 5, 6],
                [9, 1, 2, 3, 4, 5, 7, 8, 9],
            ]
        )

        oczekiwany_wynik = [(1, 9)]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_Nr36_sudoku_argumenty_tablica(self):
        wynik = sudoku(
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 2, 8, 4, 5, 3, 7],
                [2, 8, 7, 6, 3, 5, 4, 1, 9],
                [3, 4, 5, 1, 7, 9, 2, 8, 6],
            ]
        )

        oczekiwany_wynik = [(6, 9)]
        self.assertIn(wynik, oczekiwany_wynik)
