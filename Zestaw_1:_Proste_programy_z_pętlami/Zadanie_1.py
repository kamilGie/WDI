# ====================================================================================================>
# Zadanie 1
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.
# ====================================================================================================>


def Zadanie_1(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                print(a, b, c)


Zadanie_1(5)
