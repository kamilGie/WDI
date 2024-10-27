def iloczyn(li, n, res = 0, p = 0):
    if n == res: return True
    if res > n: return False
    if p == len( li ): return False

    if n % li[p] == 0: return iloczyn(li, n // li[p], res * li[p], p + 1)
    return iloczyn(li, n, res, p + 1)

l = [4,1,5,7,9,4,5,9,6,5,3,2,7,6,1,1,7,9,9,1]

print( iloczyn(l, 24) )

