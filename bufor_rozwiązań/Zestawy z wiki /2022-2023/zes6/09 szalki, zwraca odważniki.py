
def waga2(li, n, res = [], p = 0) :
    if n == 0:
        print( res )
        return True
    if p == len( li ): return False
    return waga2(li, n - li[p], res + [ li[p] ], p + 1 ) or waga2(li, n, res, p + 1) or waga2(li, n + li[p], res + [ -1 * li[p] ], p + 1)

