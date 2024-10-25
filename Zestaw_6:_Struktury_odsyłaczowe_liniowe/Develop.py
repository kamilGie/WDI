from typing import Callable, List
import sys
import os
import importlib

# Można nadpisać bazową strategię i mieć jakąś domyślną
STRATEGIA_DOMYSLNA = "domyslna"

# Ustalamy ścieżkę do pliku wykonywalnego
sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
srt_folder = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../srt")
sys.path.append(srt_folder)

# Numer zadania na podstawie nazwy pliku
nr_zadania = (os.path.basename(sciezka_pliku_wykonalnego)
              .replace("prototyp", "")
              .replace(".py", "")
              .replace("Backup", "")
              )

def stworz_zadanie(funkcje: List[Callable], strategia: str = STRATEGIA_DOMYSLNA) -> None:
    """
    Tworzy folder z rozwiązaniem na podstawie przekazanych funkcji.

    Args:
        funkcje (List[Callable]): Lista funkcji do przetworzenia.
        strategia (str): Nazwa strategii. Domyślnie 'bazowa'.
    """
    try:
        importlib.import_module("StworzZadanie").stworz_zadanie(sciezka_pliku_wykonalnego, nr_zadania, funkcje, strategia)
    except ImportError as e:
        print(f"Błąd importu modułu: {e}")

def komenda(k: str, *args: List[str], **kwargs: dict):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    try:
        return importlib.import_module("WykonajKomende").wykonaj_komende(k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs)
    except ImportError as e:
        print(f"Błąd importu modułu: {e}")
    except Exception as e:
        print(f"Wystąpił błąd podczas wykonywania komendy: {e}")
