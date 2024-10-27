# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
# odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce

def waga(li, n, p = 0 ): # li - lista odważników, n - szukana waga, p - numer branego odważnika
    if n  == 0: return True
    if p == len(li): return False
    return waga(li, n - li[p], p + 1) or waga(li, n, p + 1)
#end def




def f(T,i,r): # r - remaining
    n = len(T)
    if r == 0: return True
    if r < 0 or i > n - 1: return False

    return f(T, i + 1, r) or f(T, i + 1, r - T[i])
           #  nie biorę         biorę




odw = [1,3,5,10,16,24]
print( waga(odw, 13,) )
print( f(odw, 0, 13))