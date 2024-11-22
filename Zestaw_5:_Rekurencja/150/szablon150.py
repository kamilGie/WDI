# ====================================================================================================>
# Zadanie 150
# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie
# muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375,17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
# ====================================================================================================>


def new_number_prime(a, b): ...


if __name__ == "__main__":
    from testy150 import odpal_testy

    new_number_prime(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
