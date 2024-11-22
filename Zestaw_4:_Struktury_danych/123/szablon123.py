# ====================================================================================================>
# Zadanie 123
# Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy wy-
# stępujące w tablicy ciągi arytmetyczne(LA) i geometryczne (LG) o długości większej niż 2.
# Funkcja powinna zwrócić wartość 1 gdy LA>LG, wartość -1 gdy LA<LG oraz 0 gdy LA=LG.
# ====================================================================================================>


def leng_of_longest_geometric_subsequence(sequence): ...


if __name__ == "__main__":
    from testy123 import odpal_testy

    leng_of_longest_geometric_subsequence(int(input('Podaj sequence: ')))

    # odpal_testy()
