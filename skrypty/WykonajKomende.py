import os
import importlib
import inspect
from utils import add_sys_path


def wykonaj_komende(komenda, sciezka, nr_zadania, *args, **kwargs):
    katalog_pliku = os.path.dirname(os.path.abspath(__file__))
    sciezka_do_komendy = os.path.join(katalog_pliku, "Komendy")

    with add_sys_path(sciezka_do_komendy):
        try:
            modul = importlib.import_module(komenda)
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
    user_input = input("Podaj komendę oraz argumenty oddzielone spacją: ")
    parts = user_input.split()
    komenda = parts[0]
    argumenty = parts[1:]
    wykonaj_komende(komenda, None, None, *argumenty)
