# ====================================================================================================>
# Zadanie 69
# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
# znacza długość najdłuższego, spójnego podciągu arytmetycznego.
# ====================================================================================================>


def longest_increasing_series(tab): ...


if __name__ == "__main__":
    from testy69 import odpal_testy

    longest_increasing_series(int(input('Podaj tab: ')))

    # odpal_testy()
