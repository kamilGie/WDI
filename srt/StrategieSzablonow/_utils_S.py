import inspect


def funkcja_input(funkcja):
    """
    Zwraca string reprezentujący wywołanie zadanej funkcji `funkcja`,
    gdzie każdy parametr jest dynamicznie pobierany od użytkownika za pomocą `input`.
    Wynikiem jest wywołanie np. 'mojafunkcja(input('Podaj parametr1: '), input('Podaj parametr2: '))'.
    """
    parameters = inspect.signature(funkcja).parameters
    input_lines = [f"input('Podaj {name}: ')" for name in parameters.keys()]
    return f"    {funkcja.__name__}({', '.join(input_lines)})\n"


def parsuj_prototyp(linie_prototypu, funkcje):
    """
    Pobiera wszystkie komentarze początkowe, a następnie dodaje nagłówki funkcji
    (z zadanych funkcji w `funkcje`) i zamienia ich ciało na '...'.
    Kończy przetwarzanie po napotkaniu `if __name__ == "__main__"`.
    """
    res = ""
    wstep = True
    for linia in linie_prototypu:
        if wstep:
            if linia.strip().startswith("#"):
                res += linia
            else:
                wstep = False
        elif any(linia.startswith(f"def {f.__name__}") for f in funkcje):
            res += "\n\n" + linia.replace("\n", "") + " ...\n\n"
        elif 'if __name__ == "__main__":\n' in linia:
            return res
    return res


def main(nr_zadania, cialo_maina="\n\n"):
    """
    Generuje blok `main`. Pozwala na dodanie niestandardowego
    kodu `cialo_maina`, jeśli środek bloku `main` wymaga specyficznych operacji.
    """
    res = '\nif __name__ == "__main__":\n'
    res += f"    from testy{nr_zadania} import odpal_testy\n"
    res += cialo_maina
    res += f"\n    # odpal_testy()\n"
    return res
