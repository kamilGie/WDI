# ====================================================================================================>
# Zadanie 54
# Proszę napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
# ułamka a/b uwzględniając ułamki okresowe. Na przykład 2/3 = 0.(6),1/5 = 0.2,1/6 = 0.1(6),1/7 =
# 0.(142857)
# ====================================================================================================>


def Zadanie_54(a, b): ...


if __name__ == "__main__":
    from testy54 import odpal_testy

    Zadanie_54(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
