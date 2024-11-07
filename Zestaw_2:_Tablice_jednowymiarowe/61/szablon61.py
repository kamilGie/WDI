# ====================================================================================================>
# Zadanie 61
# Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
# ====================================================================================================>
# same_digits(123,321) -> return True


def same_digits(a, b): ...


if __name__ == "__main__":
    from testy61 import odpal_testy

    same_digits(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
