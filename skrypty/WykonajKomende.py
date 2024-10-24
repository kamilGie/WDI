import os
import importlib
import inspect
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


def wykonaj_komende(komenda, sciezka, nr_zadania, *args, **kwargs):
    """
    Wykonuje określoną komendę, ładowując odpowiedni moduł i wywołując funkcję.

    Args:
        komenda (str): Nazwa komendy do wykonania, odpowiadająca nazwie funkcji w module.
        sciezka (str): Ścieżka do pliku wykonywalnego, która może być przekazywana do komendy.
        nr_zadania (str): Numer zadania, który może być przekazywany do komendy.
        *args: Dodatkowe argumenty, które będą przekazywane do funkcji komendy.
        **kwargs: Dodatkowe argumenty kluczowe, które będą przekazywane do funkcji komendy.

    Notes:
        Komenda może być zdefiniowana w pliku o nazwie '{komenda}.py' w folderze "Komendy"
        lub w module "_skroty". Funkcja sprawdza, który z tych plików zawiera
        odpowiednią implementację komendy.

        Lista dostępnych komend jest opisana w pliku README.
    """
    katalog_pliku = os.path.dirname(os.path.abspath(__file__))
    sciezka_do_komend = os.path.join(katalog_pliku, "Komendy")

    with add_sys_path(sciezka_do_komend):
        try:
            # komenda moze byc w 2 miejsach albo w swoim pliku albo w _skroty
            if os.path.exists(os.path.join(sciezka_do_komend, f"{komenda}.py")):
                modul = importlib.import_module(komenda)
            else:
                modul = importlib.import_module("_skroty")

            funkcja = getattr(modul, komenda)

            sygnatura = inspect.signature(funkcja)
            if "sciezka" in sygnatura.parameters:
                kwargs["sciezka"] = sciezka
            if "nr_zadania" in sygnatura.parameters:
                kwargs["nr_zadania"] = nr_zadania

            funkcja(*args, **kwargs)
        except ImportError as e:
            raise ImportError(f"Nie można wykonać '{komenda}'. Szczegóły: {e}")
        except AttributeError:
            raise AttributeError(f"Moduł '{komenda}' nie zawiera funkcji '{komenda}'.")
        except Exception as e:
            raise RuntimeError(f"Wystąpił błąd podczas wykonywania '{komenda}': {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        user_input = input("Podaj komendę oraz argumenty oddzielone spacją: ")
        parts = user_input.split()
    else:
        parts = sys.argv[1:]
    komenda = parts[0]
    argumenty = parts[1:]
    wykonaj_komende(komenda, None, None, *argumenty)
