import pdfplumber
import os
from utils import PrototypBezTresci, Tresci, Develop


def StworzPlikiPython(zawartosc, pelnaSciezka):
    sciezka_pliku = os.path.join(pelnaSciezka)
    try:
        with open(sciezka_pliku, "w") as plik:
            plik.write(zawartosc)
    except IOError as e:
        print(f"Nie udało się zapisać pliku {sciezka_pliku}: {e}")


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
    with pdfplumber.open("../ZbiorZadan.pdf") as pdf:
        # lacze cale strony zbioru zadan po za ostatnimy 2 literami bo to numery strony
        TextCalegoZbioru = "".join(page.extract_text()[:-2] for page in pdf.pages)

        Zestawy = PodzielTextNaZestawy(TextCalegoZbioru)

        nrZadania = 1
        for zestaw in Zestawy:
            PoczatekNastZad = zestaw.find("Zadanie")
            nazwaZestawu = zestaw[:PoczatekNastZad].replace(" ", "_").replace("\n", "")
            os.makedirs("../" + nazwaZestawu)

            StworzPlikiPython(
                Develop(),
                f"../{nazwaZestawu}/Develop.py",
            )
            while PoczatekNastZad != -1:
                zestaw = zestaw[PoczatekNastZad:]
                PoczatekNastZad = zestaw.find(f"Zadanie {nrZadania+1}.")
                if PoczatekNastZad == -1:  # czasami pdf reader usuwa spacje pomiedzy
                    PoczatekNastZad = zestaw.find(f"Zadanie{nrZadania+1}.")

                StworzPlikiPython(
                    Tresci(zestaw[:PoczatekNastZad], nrZadania)
                    + PrototypBezTresci(nrZadania),
                    f"../{nazwaZestawu}/prototyp{nrZadania:02}.py",
                )
                nrZadania += 1


if __name__ == "__main__":
    Skrypt()
