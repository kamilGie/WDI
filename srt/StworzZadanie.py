import os
import sys
from typing import List, Callable
import importlib


class Zadanie:
    def __init__(
        self,
        linie_prototypu: List[str],
        sciezka_zadania: str,
        nr_zadania: str,
        funkcje: List[Callable],
    ):
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

    def stworz_plik(self, nazwa: str, folder: str):
        if nazwa == "brak":
            return
        try:
            sciezka_szablonu = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), folder
            )
            sys.path.append(sciezka_szablonu)
            modul = importlib.import_module(nazwa)
            generator_dokumentu = getattr(modul, nazwa)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Nie można zaimportować szablonu '{nazwa}': {e}")
        Generator_dokumentu = generator_dokumentu(
            self.linie_prototypu, self.nr_zadania, self.funkcje, self.sciezka_zadania
        )
        sciezka_rozwiazania = os.path.join(
            self.sciezka_zadania, Generator_dokumentu.nazwa_pliku
        )

        with open(sciezka_rozwiazania, "w") as file:
            file.write(str(Generator_dokumentu))


def stworz_zadanie(
    sciezka_prototypu: str,
    nr_zadania: str,
    funkcje: List[Callable],
    szablon: str,
    rozwiazanie: str,
    testy: str,
    README: str,
):
    """
    Tworzy zadanie na podstawie prototypu oraz strategii.

    Args:
        sciezka_prototypu (str): Ścieżka do pliku prototypu.
        nr_zadania (str): Numer zadania (np. 'prototyp01').
        funkcje (List[Callable]): Lista funkcji do wykorzystania w zadaniu.
        szablon (str): Nazwa klasy która ma tworzyc plik szablonu
        rozwiazanie (str): nazwa klasy która ma tworzyc plik rozwiazanie
        testy (str): nazwa klasy która  ma tworzyc plik testow
        README (str): Nazwa klasy która ma tworzyc plik szablonu

    Raises:
        ImportError: Jeśli klasy nie może być zaimportowana.
    """

    sciezka_zadania = os.path.dirname(sciezka_prototypu)
    sciezka_zadania = os.path.join(sciezka_zadania, nr_zadania)
    with open(sciezka_prototypu, "r") as file:
        linie_prototypu = file.readlines()
    zadanie = Zadanie(linie_prototypu, sciezka_zadania, nr_zadania, funkcje)

    zadanie.stworz_plik(testy, "Testy")
    zadanie.stworz_plik(README, "README")
    zadanie.stworz_plik(rozwiazanie, "Rozwiazanie")
    zadanie.stworz_plik(szablon, "Szablon")

    # Jeśli piszemy na prototypie, który nie jest backupem, stwórz z niego backup i usuń
    # zmiana nazwy nie dzialala zawsze z gitem wiec lepiej usunac i stworzyc nowe
    if "Backup" not in sciezka_prototypu:
        os.remove(sciezka_prototypu)
        sciezka_backupu = os.path.join(
            os.path.dirname(sciezka_prototypu), f"prototypBackup{nr_zadania}.py"
        )
        print("Backup prototypu zostal stworzony w", sciezka_backupu)
        with open(sciezka_backupu, "w") as file:
            file.writelines(linie_prototypu)
