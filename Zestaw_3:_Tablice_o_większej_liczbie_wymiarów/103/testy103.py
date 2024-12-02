import unittest
from contextlib import redirect_stdout
import io

from szablon103 import Zadanie_103


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
    import os
    import sys
    import importlib
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_103(self):
            self.assertEqual(Zadanie_103([[[[0, 1, 2], [3, 4, 5], [6, 7, 8]],               [[0, 1, 2], [3, 4, 5], [6, 7, 8]],               [[0, 1, 2], [3, 4, 5], [6, 7, 8]]],               [[[0, 1, 2], [3, 4, 5], [6, 7, 8]],               [[8, 6, 8], [6, 8, 6], [8, 6, 8]],               [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]]), True)

    def test_Nr02_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [2, 15, 7],        [4, 8, 21],        [6, 12, 3]    ],    [        [10, 9, 5],        [14, 25, 16],        [18, 22, 27]    ],    [        [5, 7, 11],        [13, 17, 19],        [23, 29, 31]    ]]), False)

    def test_Nr03_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [4, 9, 14, 7],        [8, 21, 10, 6],        [15, 11, 28, 12],        [3, 5, 20, 16]    ],    [        [6, 4, 18, 7],        [5, 8, 14, 12],        [10, 27, 9, 25],        [3, 15, 22, 24]    ],    [        [2, 14, 6, 8],        [12, 9, 4, 7],        [25, 10, 15, 18],        [21, 11, 30, 5]    ],    [        [3, 6, 12, 9],        [18, 24, 15, 10],        [5, 20, 30, 14],        [8, 7, 4, 2]    ]]), False)

    def test_Nr04_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [4, 6],        [8, 10]    ],    [        [12, 14],        [16, 18]    ]]), True)

    def test_Nr05_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [2, 3, 5, 7, 11],        [13, 17, 19, 23, 29],        [31, 37, 41, 43, 47],        [53, 59, 61, 67, 71],        [73, 79, 83, 89, 97]    ],    [        [101, 103, 107, 109, 113],        [127, 131, 137, 139, 149],        [151, 157, 163, 167, 173],        [179, 181, 191, 193, 197],        [199, 211, 223, 227, 229]    ],    [        [233, 239, 241, 251, 257],        [263, 269, 271, 277, 281],        [283, 293, 307, 311, 313],        [317, 331, 337, 347, 349],        [353, 359, 367, 373, 379]    ],    [        [383, 389, 397, 401, 409],        [419, 421, 431, 433, 439],        [443, 449, 457, 461, 463],        [467, 479, 487, 491, 499],        [503, 509, 521, 523, 541]    ],    [        [547, 557, 563, 569, 571],        [577, 587, 593, 599, 601],        [607, 613, 617, 619, 631],        [641, 643, 647, 653, 659],        [661, 673, 677, 683, 691]    ]]), True)

    def test_Nr06_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [4, 6, 8],        [10, 12, 14],        [16, 18, 20]    ],    [        [22, 24, 26],        [28, 30, 32],        [34, 36, 38]    ],    [        [40, 42, 44],        [46, 48, 50],        [52, 54, 56]    ]]), True)

    def test_Nr07_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [4, 6, 8, 10],        [12, 14, 16, 18],        [20, 22, 24, 26],        [28, 30, 32, 34]    ],    [        [5, 7, 9, 11],        [13, 15, 17, 19],        [21, 23, 25, 27],        [29, 31, 33, 35]    ],    [        [2, 4, 6, 8],        [10, 12, 14, 16],        [18, 20, 22, 24],        [26, 28, 30, 32]    ],    [        [3, 5, 7, 9],        [11, 13, 15, 17],        [19, 21, 23, 25],        [27, 29, 31, 33]    ]]), False)

    def test_Nr08_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [2, 3, 4],        [5, 6, 7],        [8, 9, 10]    ],    [        [11, 12, 13],        [14, 15, 16],        [17, 18, 19]    ],    [        [20, 21, 22],        [23, 24, 25],        [26, 27, 28]    ]]), False)

    def test_Nr09_Zadanie_103(self):
            self.assertEqual(Zadanie_103([    [        [9, 12, 15, 18],        [21, 24, 27, 30],        [33, 36, 39, 42],        [45, 48, 51, 54]    ],    [        [7, 14, 21, 28],        [35, 42, 49, 56],        [63, 70, 77, 84],        [91, 98, 105, 112]    ],    [        [2, 4, 6, 8],        [10, 12, 14, 16],        [18, 20, 22, 24],        [26, 28, 30, 32]    ],    [        [11, 22, 33, 44],        [55, 66, 77, 88],        [99, 110, 121, 132],        [143, 154, 165, 176]    ]]), True)


