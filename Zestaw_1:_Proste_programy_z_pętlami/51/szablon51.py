# ====================================================================================================>
# Zadanie 51
# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej licz-
# bie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każ-
# dej z liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby
# 12375,17523,75123,17253, itd. Proszę napisać funkcję która wyznaczy `ile` liczb pierwszych można zbudować
# z dwóch zadanych liczb.
# ====================================================================================================>
# return int( ilosci znalezionych tych liczb w)


def Zadanie_51(a, b): ...


if __name__ == "__main__":
    from testy51 import odpal_testy

    Zadanie_51(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
