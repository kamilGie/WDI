import os
from typing import List, Callable
from Bazowa import Bazowa as bb
from typing import Type
import Strategie


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

    def stworz_plik(self, generator_dokumentu: Type[bb]):
        Generator_dokumentu = generator_dokumentu(
            self.linie_prototypu, self.nr_zadania, self.funkcje, self.sciezka_zadania
        )
        sciezka_rozwiazania = os.path.join(
            self.sciezka_zadania, Generator_dokumentu.nazwa_pliku
        )
        with open(sciezka_rozwiazania, "w") as file:
            file.write(str(Generator_dokumentu))


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
        funkcja_ze_strategiami = getattr(Strategie, strategia)
        nowe_pliki = funkcja_ze_strategiami()
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Nie można zaimportować strategii '{strategia}': {e}")

    sciezka_zadania = os.path.dirname(sciezka_prototypu)
    sciezka_zadania = os.path.join(sciezka_zadania, nr_zadania)

    with open(sciezka_prototypu, "r") as file:
        linie_prototypu = file.readlines()

    zadanie = Zadanie(linie_prototypu, sciezka_zadania, nr_zadania, funkcje)

    for plik in nowe_pliki:
        zadanie.stworz_plik(plik)

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
