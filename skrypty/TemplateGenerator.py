def Tresci(zadanie, nrZadania):
    obramowka = "# ====================================================================================================>\n"
    zadanie_tresc = zadanie[zadanie.find(".") + 2 :].replace("\n", "\n# ")

    # czasami to sie przedluzalo nwm czemu ale to naprawia xd
    if zadanie_tresc[-2] == "#":
        zadanie_tresc = zadanie_tresc[:-3]

    return (
        f"{obramowka}" f"# Zadanie {nrZadania}\n" f"# {zadanie_tresc}\n" f"{obramowka}"
    )


def SzablonBezTresci(nrZadania):
    return f"""\n\ndef Zadanie_{nrZadania}(): ...\n\n
if __name__ == "__main__":
    from testy{nrZadania} import StworzTesty

    Zadanie_{nrZadania}()
    # StworzTesty()
"""


def ImportSkrypuTworzeniaTestow(nrZadania):
    return f"""import sys
import os
import importlib
### TU BEDA TESTY ###


sys.path.append(
    os.path.join(
        os.path.abspath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
        ),
        "skrypty",
    )
)


def StworzTesty():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(current_dir)
    path_parts = full_path.split(os.sep)
    sciezka_do_folderu = os.path.join(path_parts[-2], path_parts[-1])

    importlib.import_module("StworzTesty").StworzTesty({nrZadania}, sciezka_do_folderu)"""


def GenerujTest(nrZadania):
    return f"""import unittest
import io
from contextlib import redirect_stdout

from szablon{nrZadania} import Zadanie_{nrZadania}


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
# oczekiwne wyniki sa w tablicy zeby moc akceptowac kilka mozliwych dobrych wynikow w roznej kolejnosci/formacie np ["(1,2)","1 2","1\\n2\\n"]
# print(f"{{repr(wynik)}}") # Przydaje sie, wyświetla wynik wraz z niewidocznymi znakami (np"\\t1\\n2\\n3\\n") gotowe do wklejenia do oczekiwanego_wyniku
class Testy{nrZadania}(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_{nrZadania}()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_zwracania(self):
        wynik = Zadanie_{nrZadania}()

        oczekiwany_wynik = [None]
        self.assertIn(wynik, oczekiwany_wynik)


def odpalTesty():
    suite = unittest.TestLoader().loadTestsFromTestCase(Testy{nrZadania})
    unittest.TextTestRunner(verbosity=2).run(suite)
"""
