# 1A.
# Dwie liczby naturalne większe od 1 są zgodne jeżeli dzielą się przez te same
# liczby pierwsze.  Przykładem zgodnych liczb są pary:
#     (6, 24), (40, 50), (13, 169), (44, 242)
# nie są zgodne np. pary:
#     (6, 8), (40, 60), (13, 39), (44, 99)
#
# Tablica T została wypełniona liczbami z zakresu [2..999]. Sąsiadami pola o
# indeksie i w tablicy są pola o indeksie j, gdy abs(i-j) < 3.
# Proszę napisać funkcję zgodne(T), która dla tak wypełnionej tablicy zwraca
# liczbę elementów mających przynajmniej jednego zgodnego sąsiada. Po wykonaniu
# funkcji tablica nie musi pozostać nie zmieniona.
# Na przykład dla tablicy:  T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
# funkcja powinna zwrócić wartość 7 (są to liczby 2, 4, 6, 24, 12, 15, 45).

"""
-------------- OPIS METODY ------------------
Funkcja iteruje przez tablicę dokładnie raz. Maksymalna różnica indeksów wynosi 2, więc dla danej liczby możemy
porównać ją z liczbą o 1 lub 2 na prawo. Definiujemy tablicę, która zapisuje, czy liczba ma zgodnego sąsiada. Przy znalezieniu
liczb zgodnych zapisujemy od razu liczby z indeksami i oraz j. Program zwraca ilość wartości poprawnych z tablicy pomocniczej.
"""


def weryf(a, b):  # Funkcja weryfikuje, czy zadane dwie liczby są zgodne.
    d = 2

    while (
        a > 1 and b > 1
    ):  # w momencie, gdy którakolwiek liczba osiągnie 1 lub 0, nie będzie się dalej dzielić
        if a % d == 0 and b % d == 0:
            while a % d == 0:
                a //= d
            while b % d == 0:
                b //= d
        if (
            a % d == 0 or b % d == 0
        ):  # Jeśli poprzedni if się nie aktywował, a ten tak, wówczas jedna z liczb się dzieli, druga nie => nie są zgodne
            return False
        d += 1

    if (
        a > 1 or b > 1
    ):  # Jeśli zachodzi, któraś z liczb posiada czynnik 1szy, którego druga nie posiada.
        return False
    return True


def zgodne(T: list[int]):
    l = len(T)
    if l < 2:
        return 0  # edge case: tablica pusta lub 1-elementowa nie może zawierać zgodnych sąsiadów
    pom = [0] * l  # pom[i] określa, czy liczba T[i] ma zgodnego sąsiada

    for i in range(l - 2):
        if weryf(T[i], T[i + 1]):
            pom[i] = pom[i + 1] = 1
        if weryf(T[i], T[i + 2]):
            pom[i] = pom[i + 2] = 1

    if weryf(T[-1], T[-2]):  # edge case: powyższy for nie porównuje 2 ostatnich liczb.
        pom[-1] = pom[-2] = 1

    return sum(
        pom
    )  # sumujemy zapisane jedynki,  każda reprezentuję liczbę mającą zgodnego sąsiada


# rozwiązanie by Piotr Polański
