import pdfplumber
import os


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


def StworzPlikPython(zadanie, nrZadania, nazwaZestawu):
    obramowka = "# ====================================================================================================>\n"
    zadanie_tresc = zadanie[zadanie.find(".") + 2 :].replace("\n", "\n# ")

    if zadanie_tresc[-2] == "#":
        zadanie_tresc = zadanie_tresc[:-3]

    zawartoscPliku = (
        f"{obramowka}"
        f"# Zadanie {nrZadania}\n"
        f"# {zadanie_tresc}\n"
        f"{obramowka}\n\n"
        f"def Zadanie_{nrZadania}(): ...\n\n\n"
        f"Zadanie_{nrZadania}()\n"
    )

    sciezka_pliku = os.path.join(nazwaZestawu, f"Zadanie_{nrZadania:02}.py")
    try:
        with open(sciezka_pliku, "w") as plik:
            plik.write(zawartoscPliku)
    except IOError as e:
        print(f"Nie udało się zapisać pliku {sciezka_pliku}: {e}")


def Skrypt():
    with pdfplumber.open("ZbiorZadan.pdf") as pdf:
        TextCalegoZbioru = "".join(page.extract_text()[:-2] for page in pdf.pages)

        Zestawy = PodzielTextNaZestawy(TextCalegoZbioru)

        nrZadania = 1
        for zestaw in Zestawy:
            PoczatekNastZad = zestaw.find("Zadanie")
            nazwaZestawu = zestaw[:PoczatekNastZad].replace(" ", "_").replace("\n", "")
            os.makedirs(nazwaZestawu, exist_ok=True)

            while PoczatekNastZad != -1:
                zestaw = zestaw[PoczatekNastZad:]
                PoczatekNastZad = zestaw.find(f"Zadanie {nrZadania+1}.")
                if PoczatekNastZad == -1:  # czasami pdf reader usuwa spacje pomiedzy
                    PoczatekNastZad = zestaw.find(f"Zadanie{nrZadania+1}.")

                StworzPlikPython(zestaw[:PoczatekNastZad], nrZadania, nazwaZestawu)
                nrZadania += 1


if __name__ == "__main__":
    Skrypt()
