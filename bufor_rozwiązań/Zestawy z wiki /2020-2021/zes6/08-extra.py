li = [2,3,4,5]

def waga(li, n, p, t):
    if n == 0:
        print(t)
        return True
    if p == len(li):
        return False
    
    return waga(li, n-li[p], p+1, [*t, li[p]]) or waga(li, n, p+1, [*t]) or waga(li, n+li[p], p+1, [*t, -li[p]])


print(waga(li, 8, 0, []))