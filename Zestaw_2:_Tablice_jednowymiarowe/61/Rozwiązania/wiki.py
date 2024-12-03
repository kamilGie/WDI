# ====================================================================================================>
# Zadanie 61
# Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
# ====================================================================================================>
# same_digits(123,321) -> return True


def same_digits(a, b):
    tab = [0 for _ in range(0, 10)]

    while a > 0:
        tab[a % 10] += 1
        a = a // 10
    # end while

    while b > 0:
        tab[b % 10] -= 1
        b = b // 10
    # end while

    for element in tab:
        if element != 0:
            return False
    # end for
    return True


# --- main


