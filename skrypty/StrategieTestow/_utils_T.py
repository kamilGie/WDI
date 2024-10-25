RAMKA = "# ====================================================================================================>\n"


def GoraKlasyTestow(nr_zadania, funkcje):
    funkcjeStr = ", ".join(funkcja.__name__ for funkcja in funkcje)
    return f"""import unittest
import io
import os
import sys
from contextlib import redirect_stdout
import importlib

from szablon{nr_zadania} import {funkcjeStr}


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2).run(suite)


def komenda(k: str, *args, **kwargs):
    \"\"\"
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    \"\"\"
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    skrypty_dir = os.path.join(
        os.path.dirname(sciezka_pliku_wykonalnego), "../../skrypty"
    )
    sys.path.append(skrypty_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):"""


def metoda_zwracajaca_testow(NazwaTestu, numerTestu, zmienne, wynikWywolania):
    return f"""\n
    def test_Nr{numerTestu}_{NazwaTestu}_argumenty_{'_'.join(map(str, zmienne))}(self):
        wynik  = {NazwaTestu}({', '.join(map(str, zmienne))})

        oczekiwany_wynik = [{ wynikWywolania }]
        self.assertIn(wynik, oczekiwany_wynik)"""


def metoda_nasluchujaca_testow(NazwaTestu, numerTestu, zmienne, wynikWywolania):
    return f"""\n
    def test_Nr{numerTestu}_{NazwaTestu}_argumenty_{'_'.join(map(str, zmienne))}(self):
        f = io.StringIO()
        with redirect_stdout(f):
            {NazwaTestu}({', '.join(map(str, zmienne))})
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [{ wynikWywolania }]
        self.assertIn(wynik, oczekiwany_wynik)"""
