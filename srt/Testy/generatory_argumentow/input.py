from typing import Callable, Generator, Tuple
import inspect


def konwertuj_argument(arg):
    """Konwertuje argument na odpowiedni typ: int, float,str lub pozostaje czysty"""
    for typ in (int, float):
        try:
            return typ(arg)
        except ValueError:
            continue
    return arg


def przetwarzaj_stringa(argumenty, i, dodaj_cudzyslow=True):
    """
    Przetwarza napis z argumentów w formie tekstowej, obsługując spacje.

    Args:
        argumenty (list): Lista argumentów w formie tekstowej.
        i (int): Indeks aktualnego argumentu do przetworzenia.

    Returns:
        tuple: Krotka zawierająca:
            - wynik (str): Przetworzony napis.
            - i (int): Zaktualizowany indeks po przetworzeniu napisu.
    """
    typ_cudzyslowu = argumenty[i]
    i += 1
    fragmenty = []

    try:
        while argumenty[i] != typ_cudzyslowu:
            fragmenty.append(argumenty[i])
            i += 1
    except IndexError:
        raise ValueError(f"Nie zamknięty znak stringa dla cudzysłowu: {typ_cudzyslowu}")

    wynik = " ".join(fragmenty)
    if dodaj_cudzyslow:
        wynik = typ_cudzyslowu + wynik + typ_cudzyslowu
    return wynik, i


def przetwarzaj_tablice(argumenty, i):
    """
    Przetwarza tablicę z argumentów w formie tekstowej, obsługując zagnieżdżone tablice.

    Args:
        argumenty (list): Lista argumentów w formie tekstowej, w której mogą występować zagnieżdżone tablice.
        i (int): Indeks aktualnego argumentu do przetworzenia.

    Returns:
        tuple: Krotka zawierająca:
            - wynik (list): Przetworzona tablica, która może zawierać inne tablice jako elementy.
            - i (int): Zaktualizowany indeks po przetworzeniu tablicy.
    """
    wynik = []
    i += 1

    while argumenty[i] != "]":
        if argumenty[i] == "[":  # znaleziono nową tablicę
            tablica, i = przetwarzaj_tablice(argumenty, i)
            wynik.append(tablica)
        elif argumenty[i] == '"' or argumenty[i] == "'":
            napis, i = przetwarzaj_stringa(argumenty, i, dodaj_cudzyslow=False)
            wynik.append(napis)
        else:
            wynik.append(konwertuj_argument(argumenty[i]))
        i += 1

    return wynik, i


def przetwarzaj_wejscie(wejscie):
    """
    Przetwarza wejście w formie tekstowej na strukturę danych (listę), obsługując zagnieżdżone tablice.

    Args:
        wejscie (str): Tekstowe wejście do przetworzenia, zawierające argumenty i tablice.

    Returns:
        list: Lista przetworzonych argumentów, gdzie tablice są reprezentowane jako zagnieżdżone listy.
    """
    # W przyszlosci mozliwe ze projekt przejdzie  na wyrazenia regularne ale narazie dla czytelnosci zostawiam to
    wejscie = (
        wejscie.replace(",", " ")
        .replace("]", " ] ")
        .replace("[", " [ ")
        .replace("'", " ' ")
        .replace('"', ' " ')
        .replace("\n", " ")
    )
    argumenty = wejscie.split()

    przetwarzaj = {
        "[": przetwarzaj_tablice,
        '"': przetwarzaj_stringa,
        "'": przetwarzaj_stringa,
    }

    wyniki = []
    i = 0
    while i < len(argumenty):
        if argumenty[i] in przetwarzaj:
            element, i = przetwarzaj[argumenty[i]](argumenty, i)
            wyniki.append(element)
        else:
            wyniki.append(konwertuj_argument(argumenty[i]))
        i += 1

    return wyniki


def pobierz_parametry(
    funkcja: Callable, test_index: int
) -> Generator[Tuple, None, None]:
    """
    Pobiera parametry testowe od użytkownika.

    Args:
        test_index (int): Indeks aktualnego testu.
        param_count (int): Liczba argumentów, które mają być pobrane.

    Returns:
        Tuple: Krotka z parametrami podanymi przez użytkownika.
    """
    liczba_argumentow = len(inspect.signature(funkcja).parameters)
    if liczba_argumentow == 0:
        yield ()
        return
    else:
        koncowka_argumetnow = "" if 1 == liczba_argumentow else "y"
        while True:
            wyjscie = ", lub 'stop' by zakonczyc testy" if test_index > 3 else ""
            wejscie = input(
                f"\nTest nr {test_index}\nPodaj {liczba_argumentow} argument{koncowka_argumetnow} testowe{wyjscie}: "
            )
            if wejscie == "stop":
                print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")
                return
            print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")
            yield tuple(przetwarzaj_wejscie(wejscie))
            test_index += 1
