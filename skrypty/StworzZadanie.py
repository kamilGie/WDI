import os
import importlib
from typing import List, Callable
from utils import add_sys_path


class Zadanie:
    def __init__(
        self,
        linie_prototypu: List[str],
        sciezka_zadania: str,
        nr_zadania: str,  # jest to string bo np mamy prototyp01
        funkcje: List[Callable],
    ):
        self.linie_prototypu = linie_prototypu
        self.sciezka_zadania = sciezka_zadania
        self.nr_zadania = nr_zadania
        self.funkcje = funkcje
        os.makedirs(sciezka_zadania, exist_ok=True)

    def import_strategii(self, nazwa: str, sciezka: str):
        """Importuje strategię z zadanego modułu."""
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
        """Tworzy plik z rozwiązaniem na podstawie strategii."""
        strategia = self.import_strategii(nazwa_strategii, folder_strategii)
        nazwa_pliku = f"{nazwa_pliku}{self.nr_zadania}.py"
        sciezka_rozwiazania = os.path.join(self.sciezka_zadania, nazwa_pliku)

        with open(sciezka_rozwiazania, "w") as file:
            strategia.generuj()
            file.write(strategia.res)


def stworz_zadanie(
    sciezka_prototypu: str,
    nr_zadania: str,  # jest to string bo np mamy prototyp01
    funkcje: List[Callable],
    strategia_rozwiazania: str,
    strategia_szablonow: str,
    strategia_testow: str,
):
    with open(sciezka_prototypu, "r") as file:
        linie_prototypu = file.readlines()

    sciezka_zestawu = os.path.dirname(sciezka_prototypu)
    sciezka_zadania = os.path.join(sciezka_zestawu, str(nr_zadania))

    zadanie = Zadanie(linie_prototypu, sciezka_zadania, nr_zadania, funkcje)
    zadanie.stworz_plik(strategia_rozwiazania, "StrategieRozwiazania", "rozwiazanie")
    zadanie.stworz_plik(strategia_szablonow, "StrategieSzablonow", "szablon")
    zadanie.stworz_plik(strategia_testow, "StrategieTestow", "testy")

    # jesli piszemy na prototypie ktory nie jest backupem stworze z niego backup i usun
    if "Backup" not in sciezka_prototypu:
        os.remove(sciezka_prototypu)
        with open(sciezka_zestawu + f"/prototypBackup{nr_zadania}.py", "w") as file:
            file.writelines(linie_prototypu)
