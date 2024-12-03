# nie refaktoryzowalme to tylko napisalem w 15 m prosze nie oceniac plz

import os
import glob
import shutil

FOLDERY_ZADAN = [
    "Kolokwia/Kolokwium_2",
    "Kolokwia/Kolokwium_3",
    "Kolokwia/Kolokwium_3",
    "Zestaw_1:_Proste_programy_z_pętlami",
    "Zestaw_2:_Tablice_jednowymiarowe",
    "Zestaw_3:_Tablice_o_większej_liczbie_wymiarów",
    "Zestaw_4:_Struktury_danych",
    "Zestaw_5:_Rekurencja",
    "Zestaw_6:_Struktury_odsyłaczowe_liniowe",
    "Zestaw_7:_Struktury_drzewiaste",
    "Zestaw_8:_Wyszukiwanie_i_sortowanie",
]

sciezki = [f"../../{folder}" for folder in FOLDERY_ZADAN]

for folder_zadania in sciezki:
    for nr in os.listdir(folder_zadania):
        zadanie = os.path.join(folder_zadania, nr)
        if os.path.isdir(zadanie) and nr != "__pycache__":

            pliki = glob.glob(os.path.join(zadanie, "rozwiazanie*"))
            if len(pliki) == 0:
                continue
            plik_rozwiazania = os.path.join(pliki[0])
            with open(os.path.join(zadanie, "README.md"), "a") as dest:

                with open(plik_rozwiazania, "r") as src:
                    dest.write("\n```python\n")
                    linie = src.readlines()
                    while linie[0][0] == "#":
                        linie = linie[1:]

                    while linie and not linie[0].strip():
                        linie.pop(0)  # Usuń pierwszą pustą linię

                    # print(linie)
                    dest.writelines(linie)
                dest.write("\n```")
                print("zapisalem", plik_rozwiazania)

            folder_rozwiazania = os.path.join(zadanie, "Rozwiązania")
            nowa_nazwa = os.path.join(folder_zadania, "wiki.py")
            os.rename(plik_rozwiazania, nowa_nazwa)
            os.makedirs(folder_rozwiazania)
            shutil.move(nowa_nazwa, folder_rozwiazania)
