from contextlib import contextmanager
import sys


@contextmanager
def add_sys_path(new_path: str):
    """Dodaje nową ścieżkę do sys.path w kontekście."""
    sys.path.append(new_path)
    try:
        yield
    finally:
        sys.path.remove(new_path)


RAMKA = "# ====================================================================================================>\n"


def Develop():
    return f"""
from typing import Callable, List
import sys
import os
import importlib

# Ścieżka pliku, który został odpalony
sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
# Zmieniam ścieżkę importowania do skryptów
sys.path.append(os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../skrypty"))
# Wydobywam numer zadania z nazwy
nr_zadania = os.path.basename(sciezka_pliku_wykonalnego).replace("prototyp", "").replace(".py", "").replace("Backup", "")


# Funkcja stworzy folder z rozwiązaniem na podstawie funkcji, które przekażesz w liście jako 1 argument
def stworz_zadanie(
    funkcje: List[Callable],
    # mozna nadpisac tutaj bazowa strategia i miec ja inna strategie jako domyslna
    strategia_rozwiazania: str = "bazowa",
    strategia_szablonow: str = "bazowa",
    strategia_testow: str = "bazowa",
) -> None:
    importlib.import_module("StworzZadanie").stworz_zadanie(
        sciezka_pliku_wykonalnego,
        nr_zadania,
        funkcje,
        strategia_rozwiazania, strategia_szablonow, strategia_testow,
    )


# Lista komend jest w ReadMe
# Implementacja jest w folderze skrypty/komendy
# Wpisz komendę jako string jako 1 parametr oraz parametry, jakie wymaga i odpal funkcję, by uruchomić komendę
def komenda(k: str, *args, **kwargs):
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
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
