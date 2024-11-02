import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon58 import Zadanie_58


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

    def test_Nr01_Zadanie_58_argumenty_(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_58()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = {
            "0\\n1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n370\\n407\\n153\\n371\\n8208\\n1634\\n9474\\n93084\\n92727\\n54748\\n548834\\n9800817\\n4210818\\n1741725\\n9926315\\n24678050\\n24678051\\n88593477\\n146511208\\n912985153\\n472335975\\n534494836\\n4679307774\\n32164049650\\n40028394225\\n42678290603\\n49388550606\\n32164049651\\n94204591914\\n44708635679\\n82693916578\\n28116440335967"
        }
        self.assertTrue(
            set(wynik.split()) == oczekiwany_wynik
        )  # Porównanie z użyciem set
