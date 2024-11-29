# ====================================================================================================>
# Zadanie 160
# Kwadrat jest opisywany czwórką liczb całkowitych (x1 ,x2 ,y1 ,y2 ), gdzie x1 ,x2 ,y1 ,y2 ozna-
# czają proste ograniczające kwadrat x1 < x2 , y1 < y2 . Dana jest tablica T zawierająca opisy N kwadratów.
# Proszę napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienacho-
# dzących na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.
# ====================================================================================================>


def Zadanie_160(T): ...


if __name__ == "__main__":
    from testy160 import odpal_testy

    Zadanie_160(list(input("Podaj T: ")))

    # odpal_testy()
