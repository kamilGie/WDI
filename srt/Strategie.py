import os
import sys


# Dodaj wszystkie podfoldery po za komendy do sys.path
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    if "Komendy" != root:
        sys.path.append(root)

# Liczba plików tworzonych na podstawie strategii zależy od liczby zwracanych klas.
# Jeśli użyjemy strategii zwracającej 1 klasę, zostanie stworzony 1 plik.
# Możemy jednak opracować strategię zwracającą 10 klas, co pozwoli na stworzenie 10 plików zadania.
# Pliki będą miały nazwy odpowiadające nazwom folderów, z których pochodzą.
# Na przykład, jeśli w przyszłości planujemy dodać plik z wyjaśnieniami autora zadania
# lub innymi informacjami, wystarczy stworzyć dodatkowy folder z nazwą, jaką chcemy nadać plikowi,
# oraz dodać klasę dziedziczącą po bazowej, która zapisze te treści.


def testy_domyslne():
    "Aktualizowana najlepsza strategia testow"
    from Testy.Prime import Prime

    return Prime


def szablon_domyslny():
    "Aktualizowana najlepsza strategia Szablonow"
    from Szablon.input_main import input_main

    return input_main


def rozwiazania_domyslne():
    "Aktualizowana najlepsza strategia rozwiazania"
    from Rozwiazanie.mainless import mainless

    return mainless


def domyslna():
    """Zwraca domyslna wartości dla strategii czyli akutalizowna najlepsza strategie szablonów,rozwiązań i testów."""
    return (szablon_domyslny(), rozwiazania_domyslne(), testy_domyslne())


def rmain():
    "rozwiązanie main, rozwiazanie bedzie zawierac maina"
    from Rozwiazanie.importless import importless

    return (szablon_domyslny(), importless, testy_domyslne())


def tfloat():
    "wynik float ,Testy beda zaaokraglac wynik"
    from Testy.zaokraglony import Zaokraglony

    return szablon_domyslny(), rozwiazania_domyslne(), Zaokraglony


def tbez_kolejnosci():
    "Aktualizowana najlepsza strategia rozwiazania"
    from Testy.bez_kolejnosci import bez_kolejnosci

    return szablon_domyslny(), rozwiazania_domyslne(), bez_kolejnosci


def stop():
    "Testy beda sie generowac dopoki nie podasz argumentu `stop`"
    from Testy.Stop import Stop

    return szablon_domyslny(), rozwiazania_domyslne(), Stop


def meritum():
    "sama funkcja w rozwiązaniu"
    from Rozwiazanie.meritum import meritum

    return szablon_domyslny(), meritum, testy_domyslne()
