
# to jest funkcja, która nie zwraca, jakie odważniki wzięliśmy
def waga(li, n, p = 0):
    if n == 0: return True
    if p == len( li ): return False

    return waga(li, n - li[p], p + 1) or waga(li, n, p + 1) or waga(li, n + li[p], p + 1)
#end def


# funkcja, która zwraca jakie odważniki wzięliśmy
def waga2(li, n, res = [], p = 0) :
    if n == 0:
        print( res )
        return True
    if p == len( li ): return False
    return waga2(li, n - li[p], res + [ li[p] ], p + 1 ) or waga2(li, n, res, p + 1) or waga2(li, n + li[p], res + [ -1 * li[p] ], p + 1)
#end def


# funkcja z bitu
def f(T,i,r): # r - remaining
    n = len(T)
    if r == 0: return True
    if r < 0 or i > n - 1: return False

    return f(T, i + 1, r) or f(T, i + 1, r - T[i]) or f(T, i + 1, r + T[i] )
#end def



odw = [1,3,5,10,16,24]

for w in range(1,50):
    print(w, waga2(odw, w) )