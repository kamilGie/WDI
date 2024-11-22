# ====================================================================================================>
# Zadanie 164
# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę
# iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można
# założyć, że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna
# wpisać podzielniki do tablicyp pomocniczej. Przykład:60→[2,3,5]→2+3+5+2∗3+2∗5+3∗5+2∗3∗5=71
# ====================================================================================================>
# zadanie_164(60) -> print([2,3,5], 71)


def Zadanie_164(num): ...


if __name__ == "__main__":
    from testy164 import odpal_testy

    Zadanie_164(int(input('Podaj num: ')))

    # odpal_testy()
