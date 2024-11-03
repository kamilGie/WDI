# ====================================================================================================>
# Zadanie 55
# Dwie liczby naturalne są różno-cyfrowe jeżeli nieposiadają żadnej wspólnej cyfry. Proszęnapisać
# program,który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu(wzakresie2−16)
# w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
# taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
# podstawa 11 bo 123(10) =102(11) i 522(10) =435(11) .
# ====================================================================================================>
# print(podstawa) lub print("brak")


def Zadanie_55(a, b): ...


if __name__ == "__main__":
    from testy55 import odpal_testy

    Zadanie_55(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
