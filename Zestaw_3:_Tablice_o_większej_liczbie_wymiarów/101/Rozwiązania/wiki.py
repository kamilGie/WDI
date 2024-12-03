# ====================================================================================================>
# Zadanie 101
# Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca war-
# tość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
# False w przeciwnym przypadku.
# ====================================================================================================>


def Zadanie_101(tab):
    n = len(tab)
    column = [0 for i in range(n)]

    for y in range(n):
        flag = False
        for x in range(n):
            if tab[y][x] == 0:
                flag = True
                column[x] = 1
            # end if
        # end for 2
        if not flag:
            return False
        else:
            flag = True
    # end for 1

    for element in column:
        if element == 0:
            return False
    # end for
    return True


