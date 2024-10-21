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
    from testy{nrZadania} import Testy{nrZadania}

    Zadanie_{nrZadania}()
    # Testy{nrZadania}.StworzTesty([Zadanie_{nrZadania}])
"""


def ImportSkrypuTworzeniaTestow(nrZadania):
    return f"""class Testy{nrZadania}:
    @staticmethod
    def StworzTesty(f):
        import sys
        import os
        import importlib
        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../skrypty"))
        p = os.path.abspath(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        importlib.import_module("StworzTesty").StworzTesty({nrZadania},os.path.join(p[-2],p[-1]),f)"""


def GoraKlasyTestow(nrZadania):
    return f"""import unittest
import io
from contextlib import redirect_stdout

from szablon{nrZadania} import Zadanie_{nrZadania}


class Testy{nrZadania}:
    class testy(unittest.TestCase):"""


def MetodaKlasyTestow(nrZadania, zmienne, wynikWywolania):
    return f"""\n
        def test_{'_'.join(map(str, zmienne))}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_{nrZadania}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            oczekiwany_wynik = [{ repr(wynikWywolania) }]
            self.assertIn(wynik, oczekiwany_wynik)\n"""


def DolKlasyTestow(nrZadania):
    return f"""\n    @staticmethod
    def uruchom():
        suite = unittest.TestLoader().loadTestsFromTestCase(Testy{nrZadania}.testy)
        unittest.TextTestRunner(verbosity=2).run(suite)"""
