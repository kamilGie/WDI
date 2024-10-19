import pdfplumber
import os


def GenerujWstep(zadanie, nrZadania):
    obramowka = "# ====================================================================================================>\n"
    zadanie_tresc = zadanie[zadanie.find(".") + 2 :].replace("\n", "\n# ")

    # czasami to sie przedluzalo nwm czemu ale to naprawia xd
    if zadanie_tresc[-2] == "#":
        zadanie_tresc = zadanie_tresc[:-3]

    return (
        f"{obramowka}" f"# Zadanie {nrZadania}\n" f"# {zadanie_tresc}\n" f"{obramowka}"
    )


def GenerujZawartosci(nrZadania):
    return f"""\n\ndef Zadanie_{nrZadania}(): ...\n\n
if __name__ == "__main__":
    from test{nrZadania} import odpalTesty

    Zadanie_{nrZadania}()
    # odpalTesty()
"""


def GenerujTest(nrZadania):
    return f"""import unittest
import io
from contextlib import redirect_stdout

from exercise{nrZadania} import Zadanie_{nrZadania}

TESTY = False  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
# oczekiwne wyniki sa w tablicy zeby moc akceptowac kilka mozliwych dobrych wynikow w roznej kolejnosci/formacie np ["(1,2)","1 2","1\\n2\\n"]
# print(f"{{repr(wynik)}}") # Przydaje sie, wyświetla wynik wraz z niewidocznymi znakami (np"\\t1\\n2\\n3\\n") gotowe do wklejenia do oczekiwanego_wyniku
class Test{nrZadania}(unittest.TestCase):

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
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test{nrZadania})
    unittest.TextTestRunner(verbosity=2).run(suite)
"""


def StworzPlikiPython(zawartosc, pelnaSciezka):
    sciezka_pliku = os.path.join(pelnaSciezka)
    try:
        with open(sciezka_pliku, "w") as plik:
            plik.write(zawartosc)
    except IOError as e:
        print(f"Nie udało się zapisać pliku {sciezka_pliku}: {e}")


def StworzFolderZadania(FolderZadania, nrZadania, Zadanie):
    os.makedirs(FolderZadania)

    wstep = GenerujWstep(Zadanie, nrZadania)
    StworzPlikiPython(
        wstep + GenerujZawartosci(nrZadania),
        f"{FolderZadania}/exercise{nrZadania}.py",
    )
    StworzPlikiPython(
        wstep,
        f"{FolderZadania}/solution{nrZadania}.py",
    )
    StworzPlikiPython(
        GenerujTest(nrZadania),
        f"{FolderZadania}/test{nrZadania}.py",
    )


def PodzielTextNaZestawy(text):
    # usuwanie textu przed Zestawem
    numerZestawu = 1
    indexKoncaZestawu = text.find(f"Zestaw {numerZestawu}:")
    text = text[indexKoncaZestawu:]

    Zestawy = []
    while indexKoncaZestawu != -1:
        indexKoncaZestawu = text.find(f"Zestaw {numerZestawu+1}:")
        Zestawy.append(text[:indexKoncaZestawu])
        text = text[indexKoncaZestawu:]
        numerZestawu += 1
    return Zestawy


def Skrypt():
    with pdfplumber.open("ZbiorZadan.pdf") as pdf:
        # lacze cale strony zbioru zadan po za ostatnimy 2 literami bo to numery strony
        TextCalegoZbioru = "".join(page.extract_text()[:-2] for page in pdf.pages)

        Zestawy = PodzielTextNaZestawy(TextCalegoZbioru)

        nrZadania = 1
        for zestaw in Zestawy:
            PoczatekNastZad = zestaw.find("Zadanie")
            nazwaZestawu = zestaw[:PoczatekNastZad].replace(" ", "_").replace("\n", "")
            os.makedirs(nazwaZestawu)

            while PoczatekNastZad != -1:
                zestaw = zestaw[PoczatekNastZad:]
                PoczatekNastZad = zestaw.find(f"Zadanie {nrZadania+1}.")
                if PoczatekNastZad == -1:  # czasami pdf reader usuwa spacje pomiedzy
                    PoczatekNastZad = zestaw.find(f"Zadanie{nrZadania+1}.")

                StworzFolderZadania(
                    nazwaZestawu + f"/{nrZadania:02}",
                    nrZadania,
                    zestaw[:PoczatekNastZad],
                )

                nrZadania += 1


if __name__ == "__main__":
    Skrypt()
