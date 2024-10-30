import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon14 import Zadanie_14


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

    def test_Nr1_Zadanie_14_argumenty_(self):
        print("ten test trwa okolo 80 sekund")
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_14()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = "284 220\n1210 1184\n2924 2620\n5564 5020\n6368 6232\n10856 10744\n14595 12285\n18416 17296\n66992 66928\n71145 67095\n76084 63020\n87633 69615\n88730 79750\n123152 122368\n124155 100485\n139815 122265\n153176 141664\n168730 142310\n176336 171856\n180848 176272\n202444 196724\n203432 185368\n365084 280540\n389924 308620\n399592 356408\n430402 319550\n455344 437456\n486178 469028\n514736 503056\n525915 522405\n652664 643336\n669688 600392\n686072 609928\n691256 624184\n712216 635624\n783556 667964\n796696 726104\n863835 802725\n901424 879712\n980984 898216"

        self.assertEqual(wynik, oczekiwany_wynik)
