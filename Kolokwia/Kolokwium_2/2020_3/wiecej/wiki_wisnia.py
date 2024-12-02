"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami
całkowitymi. Proszę za-implementować funkcję chess(T) która ustawia na
szachownicy dwie wieże, tak aby suma liczb na „szachowanych” przez wieże polach
była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić
położenie wież w postaci krotki (row1, col1, row2, col2).
Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
"""

# Bartłomiej Wiśniewski
# Sumuję całe kolumny i wersze i odejmuję komórki nadmiernie zsumowane


def chess(T):
    sy = [0] * len(T)
    sx = [0] * len(T)

    for x in range(len(T)):
        for y in range(len(T)):
            sx[x] += T[y][x]
            sy[y] += T[y][x]

    # print(sx)
    # print(sy)

    best_s = 0
    best_x1 = 0
    best_y1 = 0
    best_x2 = 0
    best_y2 = 0

    for x1 in range(len(T)):
        for y1 in range(len(T)):
            for x2 in range(len(T)):
                for y2 in range(len(T)):

                    if x1 == x2 and y1 == y2:
                        continue

                    norm = 0
                    if x1 != x2 and y1 != y2:

                        s1 = sx[x1] + sy[y1] - 2 * T[y1][x1]
                        s2 = sx[x2] + sy[y2] - 2 * T[y2][x2]
                        norm = -T[y2][x1] - T[y1][x2]

                    elif x1 == x2 and y1 != y2:
                        s1 = sx[x1] + sy[y1]
                        s2 = sy[y2]
                        norm = -2 * T[y1][x1] - 2 * T[y2][x2]

                    elif y1 == y2 and x1 != x2:

                        s1 = sx[x1] + sy[y1]
                        s2 = sx[x2]
                        norm = -2 * T[y1][x1] - 2 * T[y2][x2]

                    if s1 + s2 + norm > best_s:
                        best_x1 = x1
                        best_y1 = y1
                        best_x2 = x2
                        best_y2 = y2
                        best_s = s1 + s2 + norm

    return best_y1, best_x1, best_y2, best_x2


# end def


def pt(t):
    for r in t:
        for e in r:
            print(e, end="\t")
        print()
    print()


arr = [[4, 0, 2], [3, 0, 0], [6, 5, 3]]
pt(arr)
print(chess(arr))  # (0,1,1,0) suma=17

arr = [[1, 1, 2, 3], [-1, 3, -1, 4], [4, 1, 5, 4], [5, 0, 3, 6]]
pt(arr)
# jak cos to nie dziala poprawnie
print(chess(arr))  # (2,3,3,1) suma=35
