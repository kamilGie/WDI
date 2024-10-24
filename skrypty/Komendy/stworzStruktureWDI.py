import pdfplumber
import os

RAMKA = "# ====================================================================================================>\n"


def Develop():
    return f"""from typing import Callable, List
import sys
import os
import importlib

# Można nadpisać bazową strategię i mieć jakąś domyślną
STRATEGIA_DOMYSLNA = "bazowa"

# Ustalamy ścieżkę do pliku wykonywalnego
sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
skrypty_folder = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../skrypty")
sys.path.append(skrypty_folder)

# Numer zadania na podstawie nazwy pliku
nr_zadania = (os.path.basename(sciezka_pliku_wykonalnego)
              .replace("prototyp", "")
              .replace(".py", "")
              .replace("Backup", "")
              )

def stworz_zadanie(funkcje: List[Callable], strategia: str = STRATEGIA_DOMYSLNA) -> None:
    \"\"\"
    Tworzy folder z rozwiązaniem na podstawie przekazanych funkcji.

    Args:
        funkcje (List[Callable]): Lista funkcji do przetworzenia.
        strategia (str): Nazwa strategii. Domyślnie 'bazowa'.
    \"\"\"
    try:
        importlib.import_module("StworzZadanie").stworz_zadanie(sciezka_pliku_wykonalnego, nr_zadania, funkcje, strategia)
    except ImportError as e:
        print(f"Błąd importu modułu: {{e}}")

def komenda(k: str, *args: List[str], **kwargs: dict):
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
    try:
        return importlib.import_module("WykonajKomende").wykonaj_komende(k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs)
    except ImportError as e:
        print(f"Błąd importu modułu: {{e}}")
    except Exception as e:
        print(f"Wystąpił błąd podczas wykonywania komendy: {{e}}")
"""


def Tresci(zadanie, nrZadania):
    zadanie_tresc = zadanie[zadanie.find(".") + 2 :].replace("\n", "\n# ")

    # czasami to sie przedluzalo nwm czemu ale to naprawia xd
    if zadanie_tresc[-2] == "#":
        zadanie_tresc = zadanie_tresc[:-3]

    return f"{RAMKA}# Zadanie {nrZadania}\n" f"# {zadanie_tresc}\n" f"{RAMKA}"


def PrototypBezTresci(nrZadania):
    return f"""\n\ndef Zadanie_{nrZadania}(): ...\n\n
if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_{nrZadania}()
    # stworz_zadanie([Zadanie_{nrZadania}])
"""


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


def Generuj():
    sciezka_katalog_glowny = os.path.join(os.path.dirname(__file__), "../../")
    with pdfplumber.open(os.path.join(sciezka_katalog_glowny, "ZbiorZadan.pdf")) as pdf:
        # lacze cale strony zbioru zadan po za ostatnimy 2 literami bo to numery strony
        TextCalegoZbioru = "".join(page.extract_text()[:-2] for page in pdf.pages)

        Zestawy = PodzielTextNaZestawy(TextCalegoZbioru)

        nrZadania = 1
        for zestaw in Zestawy:
            PoczatekNastZad = zestaw.find("Zadanie")
            nazwaZestawu = zestaw[:PoczatekNastZad].replace(" ", "_").replace("\n", "")
            os.makedirs(os.path.join(sciezka_katalog_glowny, nazwaZestawu))

            StworzPlikiPython(
                Develop(),
                os.path.join(sciezka_katalog_glowny, nazwaZestawu, "Develop.py"),
            )
            while PoczatekNastZad != -1:
                zestaw = zestaw[PoczatekNastZad:]
                PoczatekNastZad = zestaw.find(f"Zadanie {nrZadania+1}.")
                if PoczatekNastZad == -1:  # czasami pdf reader usuwa spacje pomiedzy
                    PoczatekNastZad = zestaw.find(f"Zadanie{nrZadania+1}.")

                StworzPlikiPython(
                    Tresci(zestaw[:PoczatekNastZad], nrZadania)
                    + PrototypBezTresci(nrZadania),
                    os.path.join(
                        sciezka_katalog_glowny,
                        nazwaZestawu,
                        f"prototyp{nrZadania:02}.py",
                    ),
                )
                nrZadania += 1


def stworzStruktureWDI(nr_zadania):
    # takie ubezpieczenie gdyby ktos z poziomu zadania wpisal komende
    if nr_zadania is not None:
        print(
            "Stworz Strukture WDI mozna wykonac tylko z poziomu WykonajKomende lub Maina"
        )
        return
    Generuj()


if __name__ == "__main__":
    Generuj()
