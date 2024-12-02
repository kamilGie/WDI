# ====================================================================================================>
# Zadanie 55
# Dwie liczby naturalne są różno-cyfrowe jeżeli nieposiadają żadnej wspólnej cyfry. Proszęnapisać
# program,który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu(wzakresie2−16)
# w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) =102(11) i 522(10) =435(11) .
# ====================================================================================================>
# print(podstawa) lub print("brak")

# rozwiazanie z wiki ale posiada tablice


def common_digit(a, b, s):
    tab = [False for _ in range(s)]

    while a != 0:
        tab[a % s] = True
        a = a // s
    # end while

    while b != 0:
        if tab[b % s]:
            return False
        b = b // s
    # end while
    return True


def Zadanie_55(a, b):
    for s in range(2, 17):
        if common_digit(a, b, s):
            print(s)
            break
    else:
        print("brak")


