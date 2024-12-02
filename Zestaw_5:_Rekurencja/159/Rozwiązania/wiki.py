# ====================================================================================================>
# Zadanie 159
# Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A
# cyfr 1 oraz B cyfr 0, gdzie A,B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
# ilośćwszystkichmożliwychdozbudowanialiczb,takichżepierwszacyfrawsystemiedwójkowym(najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2) ,10100(2) ,11000(2)
# ====================================================================================================>


from math import sqrt


def prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True


def Zadanie_159(A, B):
    num = 2 ** (A + B - 1)
    suma = 0

    def rek(A, B, num):
        nonlocal suma
        if A == 0 and B == 0:
            if not prime(num):
                suma += 1
                print(num)

            return
        # end if

        if A > 0:
            rek(A - 1, B, num + 2 ** (A + B - 1))
        if B > 0:
            rek(A, B - 1, num)

    # end def 2
    rek(A - 1, B, num)
    return suma
