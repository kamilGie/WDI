# ====================================================================================================>
# Zadanie 26
# Proszę napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie
# dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
# ====================================================================================================>
# a=10 b=3 n=10  -- > print(3.3333333333)
# a=5 b=2 n=10  -- > print(2.5)
# a=4 b=2 n=10  -- > print(2)


def ulamek(a, b, n): ...


if __name__ == "__main__":
    from testy26 import odpal_testy

    ulamek(int(input("Podaj a: ")), int(input("Podaj b: ")), int(input("Podaj n: ")))

    # odpal_testy()
