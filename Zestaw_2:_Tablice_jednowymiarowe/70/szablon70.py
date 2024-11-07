# ====================================================================================================>
# Zadanie 70
# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
# znacza długość najdłuższego, spójnego podciągu geometrycznego.
# ====================================================================================================>


def longest_geometric_series(tab: list): ...


if __name__ == "__main__":
    from testy70 import odpal_testy

    longest_geometric_series(int(input('Podaj tab: ')))

    # odpal_testy()
