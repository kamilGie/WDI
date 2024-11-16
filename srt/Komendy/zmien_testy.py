from StworzZadanie import stworz_zadanie
import os


def zmien_testy(
    sciezka,
    nr_zadania,
    funkcje,
    testy="domyslna",
    rozwiazanie="domyslna",
    szablon="domyslna",
):
    """
    Zeby nie modyfikowac funkcji stworz_zadanie to zmien test tworzy nowy plik na bazie
    pliku z ktorego powstala komenda o nazwie prototyp i z niej udaje ze tworzy testy xdd
    """
    nazwa_pliku = os.path.basename(sciezka)
    if "szablon" not in nazwa_pliku:
        print("zmien testy sa mozliwe tylko dla szablonow")
        return

    with open(sciezka, "r") as file:
        linie = file.readlines()

    sciezka_prototypu_stworzonego = os.path.join(
        os.path.dirname(os.path.dirname(sciezka)), f"prototyp{nr_zadania}.py"
    )
    with open(sciezka_prototypu_stworzonego, "w") as file:
        for linia in linie:
            if "komenda(" in linia or f"testy{nr_zadania}" in linia:
                continue
            file.write(linia)

    stworz_zadanie(
        sciezka_prototypu_stworzonego,
        nr_zadania,
        funkcje,
        testy=testy,
        rozwiazanie=rozwiazanie,
        szablon=szablon,
    )
