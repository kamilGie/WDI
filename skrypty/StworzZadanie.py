import os
import importlib
from typing import List, Callable
import sys
from contextlib import contextmanager
import StrategieZestawy

@contextmanager
def add_sys_path(new_path: str):
    """Dodaje nową ścieżkę do sys.path w kontekście."""
    sys.path.append(new_path)
    try:
        yield
    finally:
        sys.path.remove(new_path)

class Zadanie:
    def __init__( self, linie_prototypu: List[str], sciezka_zadania: str, nr_zadania: str,  funkcje: List[Callable]):
        """
        Inicjalizuje instancję klasy Zadanie.

        Args:
            linie_prototypu (List[str]): Lista linii prototypu.
            sciezka_zadania (str): Ścieżka do katalogu, w którym zostanie utworzone zadanie.
            nr_zadania (str): Numer zadania (np. 'prototyp01').
            funkcje (List[Callable]): Lista funkcji, które mają być wykorzystane w zadaniu.
        """
        self.linie_prototypu = linie_prototypu
        self.sciezka_zadania = sciezka_zadania
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        os.makedirs(sciezka_zadania, exist_ok=True)

    def import_strategii(self, nazwa: str, sciezka: str):
        """
        Importuje strategię z zadanego modułu.

        Args:
            nazwa (str): Nazwa strategii do zaimportowania.
            sciezka (str): Ścieżka do folderu z modułem strategii.

        Returns:
            obiekt strategii: Zwraca zaimportowaną strategię z przekazanymi argumentami.
        """
        katalog_pliku = os.path.dirname(os.path.abspath(__file__))
        sciezka_do_strategii = os.path.join(katalog_pliku, sciezka)

        with add_sys_path(sciezka_do_strategii):
            try:
                modul_strategii = importlib.import_module(f"{sciezka}.{nazwa}")
                strategia = getattr(modul_strategii, nazwa.title())
            except (ImportError, AttributeError) as e:
                raise ImportError(f"Nie można zaimportować strategii '{nazwa}': {e}")

        return strategia(
            self.linie_prototypu, self.nr_zadania, self.funkcje, self.sciezka_zadania
        )

    def stworz_plik(
        self, nazwa_strategii: str, folder_strategii: str, nazwa_pliku: str
    ):
        """
        Tworzy plik z rozwiązaniem na podstawie strategii.

        Args:
            nazwa_strategii (str): Nazwa strategii do zaimportowania.
            folder_strategii (str): Nazwa folderu, w którym znajduje się strategia.
            nazwa_pliku (str): Nazwa pliku do utworzenia (bez rozszerzenia).

        Raises:
            ImportError: Jeśli strategia nie może być zaimportowana.
        """
        strategia = self.import_strategii(nazwa_strategii, folder_strategii)
        nazwa_pliku = f"{nazwa_pliku}{self.nr_zadania}.py"
        sciezka_rozwiazania = os.path.join(self.sciezka_zadania, nazwa_pliku)

        with open(sciezka_rozwiazania, "w") as file:
            strategia.generuj()
            file.write(strategia.res)


def stworz_zadanie(
    sciezka_prototypu: str, nr_zadania: str, funkcje: List[Callable], strategia: str
):
    """
    Tworzy zadanie na podstawie prototypu oraz strategii.

    Args:
        sciezka_prototypu (str): Ścieżka do pliku prototypu.
        nr_zadania (str): Numer zadania (np. 'prototyp01').
        funkcje (List[Callable]): Lista funkcji do wykorzystania w zadaniu.
        strategia (str): Nazwa strategii do zastosowania.

    Raises:
        ImportError: Jeśli strategia nie może być zaimportowana.
    """
    try:
        s = getattr(StrategieZestawy, strategia)
        strategia_rozwiazania, strategia_szablonow, strategia_testow = s()
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Nie można zaimportować strategii '{strategia}': {e}")

    sciezka_zestawu = os.path.dirname(sciezka_prototypu)
    sciezka_zadania = os.path.join(sciezka_zestawu, str(nr_zadania))

    with open(sciezka_prototypu, "r") as file:
        linie_prototypu = file.readlines()
    zadanie = Zadanie(linie_prototypu, sciezka_zadania, nr_zadania, funkcje)
    zadanie.stworz_plik(strategia_rozwiazania, "StrategieRozwiazania", "rozwiazanie")
    zadanie.stworz_plik(strategia_szablonow, "StrategieSzablonow", "szablon")
    zadanie.stworz_plik(strategia_testow, "StrategieTestow", "testy")

    # Jeśli piszemy na prototypie, który nie jest backupem, stwórz z niego backup i usuń
    if "Backup" not in sciezka_prototypu:
        os.remove(sciezka_prototypu)
        with open(sciezka_zestawu + f"/prototypBackup{nr_zadania}.py", "w") as file:
            file.writelines(linie_prototypu)
