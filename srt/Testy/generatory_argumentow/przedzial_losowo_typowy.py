import inspect
import random


def dodaj_typowe_wartosci(dol, gora):
    """generator typowe wartosci testow dla przedzialu"""
    typowe_wartosci = [0, 1, -1, 10]

    for wartosc in typowe_wartosci:
        if all(d <= wartosc for d in dol) and all(g > wartosc for g in gora):
            yield tuple([wartosc] * len(dol))


def wygeneruj_losowe_testy(funkcja, _):
    """
    Funkcja generuje losowe testy dla podanej funkcji, na podstawie jej argumentów.
    Użytkownik podaje przedziały wartości dla każdego argumentu, a następnie testy są generowane
    na tych podstawach. Dodatkowo, funkcja dodaje testy dla typowych przypadków, takich jak same zera
    lub jedynki w argumentach. Na końcu duplikaty są usuwane, a testy są posortowane.

    Args:
        funkcja (function): Funkcja, dla której mają zostać wygenerowane testy. Funkcja ta powinna
                             posiadać argumenty, dla których zostaną określone przedziały wartości.

    Returns:
        int: Liczba wygenerowanych testów.
            Zwraca numer ostatniego testu (zaczynając od 1), jeżeli wszystko poszło pomyślnie.
            Jeśli użytkownik przerwie proces generowania testów, funkcja zwróci 0.

    Proces:
    1. Funkcja rozpoczyna generowanie testów, pytając użytkownika, czy chce używać losowych liczb.
    2. Jeśli użytkownik wybiera tak, funkcja zbiera przedziały dla każdego argumentu funkcji.
    3. Następnie generuje losowe wartości dla tych argumentów w wybranych przedziałach.
    4. Dodatkowo, jeśli wszystkie przedziały są odpowiednie, dodawane są testy z samymi zerami,
       jedynkami lub wartościami wskazanymi jako typowe przypadki w przyszlosci typowe przypadki beda rozszerzane
    5. Duplikaty testów są usuwane, a wyniki są posortowane.
    6. Na końcu dla każdej z wygenerowanych krotek uruchamiana jest funkcja testująca i do pliku jest dodawna metoda.
    """

    parametry_funkcji = inspect.signature(funkcja).parameters
    liczba_argumentow = len(parametry_funkcji)

    if liczba_argumentow == 0:
        return 0

    # losowe wartosci tylko dla  mozliwych wartosci int
    if not all(
        param.annotation is int or param.annotation is inspect.Parameter.empty
        for param in inspect.signature(funkcja).parameters.values()
    ):
        return 0

    while True:
        czy_generowac = input(
            "Czy wygenerować testy na losowych liczbach w przedziale? (y/n): "
        )
        print(f"\033[F\033[K", end="")
        if czy_generowac == "y":
            break
        elif czy_generowac == "n":
            return 0
        else:
            print(
                "Wpisz 'y' jeśli chcesz lub 'n' jeśli chcesz samodzielnie podać argumenty!"
            )

    lista_krotek = []
    dol, gora = [], []

    # Zbieramy przedziały dla każdego argumentu
    for argument in parametry_funkcji:
        while True:
            wejscie = (
                input(
                    f"Podaj przedziały DOŁU i GÓRY dla `{argument}` (oddzielone spacjami): "
                )
                or "0 1000"
            )
            try:
                przedzial = list(map(int, wejscie.split()))
            except ValueError:
                print(f"\033[F\033[K", end="")
                print("Wprowadź liczby całkowite.")
                continue

            if len(przedzial) == 1:
                d = przedzial[0]
                g = 1000
                if d > g:
                    print(f"\033[F\033[K", end="")
                    print("Dół musi być mniejszy od domyślnej góry (1000).")
                    continue
            elif len(przedzial) == 2:
                d, g = przedzial
                if d > g:
                    print(f"\033[F\033[K", end="")
                    print("Góra musi być większa od dołu.")
                    continue
            else:
                print(f"\033[F\033[K", end="")
                print("Wprowadź 2 liczby całkowite.")
                continue

            dol.append(d)
            gora.append(g)
            print(f"\033[F\033[K", end="")
            print(f"Dla {argument} argumenty będą od {d} do {g}.")
            break

    print("\n")

    # Generowanie krotek z losowymi wartościami
    for _ in range(liczba_argumentow * 30):  # Powtarzamy proces 30 razy
        losowe_wartosci = tuple(
            random.randint(dol[j], gora[j]) for j in range(len(dol))
        )
        lista_krotek.append(losowe_wartosci)

    # Dodanie typowych testów
    for typowa_wartosci in dodaj_typowe_wartosci(dol, gora):
        lista_krotek.append(typowa_wartosci)

    # Usuwanie duplikatów i sortowanie wyników
    lista_krotek = sorted(set(lista_krotek), key=lambda x: abs(sum(x)))
    for krotki in lista_krotek:
        yield krotki
    return
