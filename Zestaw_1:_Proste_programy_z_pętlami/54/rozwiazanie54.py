# ====================================================================================================>
# Zadanie 54
# Proszę napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
# ułamka a/b uwzględniając ułamki okresowe. Na przykład 2/3 = 0.(6),1/5 = 0.2,1/6 = 0.1(6),1/7 =
# 0.(142857)
# ====================================================================================================>


def Zadanie_54(a, b):
    integer_part = a // b
    a %= b

    if a == 0:
        return f"{integer_part}.0"

    digits = []
    modulo = {}

    while a > 0:
        if a in modulo:
            start_index = modulo[a]
            non_repeating = "".join(map(str, digits[:start_index]))
            repeating = "".join(map(str, digits[start_index:]))
            return f"{integer_part}.{non_repeating}({repeating})"

        # Zapisujemy pozycję obecnej reszty
        modulo[a] = len(digits)

        # Obliczamy następną cyfrę dziesiętną
        a *= 10
        digits.append(a // b)
        a %= b

    # Jeśli wyszliśmy z pętli, ułamek jest skończony
    fractional_part = "".join(map(str, digits))
    return f"{integer_part}.{fractional_part}"


