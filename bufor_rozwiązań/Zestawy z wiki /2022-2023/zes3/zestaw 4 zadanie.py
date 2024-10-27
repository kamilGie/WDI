from math import sqrt
# Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
# T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające
# liczby komplementarnej.

def czy_pierwsza(n):
    if n==2 or n==3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i < sqrt(n) + 1:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    #end
    return True


def zad13(tab):
    n = len(tab)
    for y in range(n):
        for x in range(n):
            for i in range(n):
                found = False
                for j in range(n):
                    if y == i and x == j:
                        continue
                    if tab[i][j] == 0:
                        continue
                    if czy_pierwsza( tab[y][x] + tab[i][j] ):
                        found = True
                        break
                #end for j
                if found: break

            #end for i
            else: tab[y][x] = 0
        #end for x
    #end for y
    return tab

tab = [ [2,3], [3,12] ]
print( zad13(tab) )





