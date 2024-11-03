# ====================================================================================================>
# Zadanie 26
# Proszę napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie
# dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
# ====================================================================================================>


def ulamek(a, b, n):
    print(a // b, end="")
    if a % b != 0:
        print(".", end="")
        a = a % b
        while a > 0 and n > 0:
            a = a * 10
            print(a // b, end="")
            a = a % b
            n = n - 1
