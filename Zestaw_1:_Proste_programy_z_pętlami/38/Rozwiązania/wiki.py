# ====================================================================================================>
# Zadanie 38
# Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb natural-
# nych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać te
# elementy ciągu które są równe średniej arytmetycznej z 4 najbliższych sąsiadów. Na przykład dla ciągu:
# 2,3,2,7,1,2,4,8,5,2,2,5,7,9,3,1,0 powinny zostać wypisane liczby: 4,5. Można założyć, że w ciągu znajduje się
# co najmniej 5 elementów.
# ====================================================================================================>


def Zadanie_38():
    a1, a2, a3, a4, a5 = (int(input()) for _ in range(1, 6))

    while a5 != 0:
        if (a1 + a2 + a4 + a5) / 4 == a3:
            print(f"srednia:{a3}")
        a1, a2, a3, a4, a5 = a2, a3, a4, a5, int(input())
