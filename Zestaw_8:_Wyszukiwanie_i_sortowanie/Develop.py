from typing import Callable, List


def stworz_zadanie(
    funkcje: List[Callable],
    testy="domyslne_t",
    rozwiazanie="domyslne_r",
    szablon="domyslne_s",
    README="domyslne_rm",
) -> None:
    """
    Tworzy folder z rozwiązaniem na podstawie przekazanych funkcji.

    Args:
        funkcje (List[Callable]): Lista funkcji do przetworzenia.
        szablon (str): Nazwa klasy która ma tworzyc plik szablonu
        rozwiazanie (str): nazwa klasy która ma tworzyc plik rozwiazanie
        testy (str): nazwa klasy która  ma tworzyc plik testow
    """
    # Lazy loading dla wydajności importu
    import sys
    import os

    # Ustalamy ścieżkę do pliku wykonywalnego
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])

    # Numer zadania na podstawie nazwy pliku
    nr_zadania = (
        os.path.basename(sciezka_pliku_wykonalnego)
        .replace("prototyp", "")
        .replace(".py", "")
        .replace("Backup", "")
    )
    # importjemy stworz zadanie z folderu rodzica
    srt_folder = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../srt")
    sys.path.append(srt_folder)

    # To lsp moze zaznaczac jako blad ale program bedzie dzialac . lsp nie ogarnia sys.path join,
    from StworzZadanie import stworz_zadanie

    # w przyszlosci jak projekt przejdzie na pakiety nie bedzie takiego problemu

    stworz_zadanie(
        sciezka_pliku_wykonalnego,
        nr_zadania,
        funkcje,
        szablon,
        rozwiazanie,
        testy,
        README,
    )


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
    # lazy loading dla wydajnosci importu
    import sys
    import os

    # Ustalamy ścieżkę do pliku wykonywalnego
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_folder = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../srt")
    sys.path.append(srt_folder)

    # Numer zadania na podstawie nazwy pliku
    nr_zadania = (
        os.path.basename(sciezka_pliku_wykonalnego)
        .replace("prototyp", "")
        .replace(".py", "")
        .replace("Backup", "")
    )
    from WykonajKomende import wykonaj_komende

    try:
        return wykonaj_komende(
            k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
        )
    except ImportError as e:
        print(f"Błąd importu modułu: {e}")
    except Exception as e:
        print(f"Wystąpił błąd podczas wykonywania komendy: {e}")
