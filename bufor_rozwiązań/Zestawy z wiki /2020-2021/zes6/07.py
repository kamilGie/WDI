li = [1,3,4,5]

def waga(li, n, p):
    if n == 0:
        return True
    if p == len(li):
        return False
    
    return waga(li, n-li[p], p+1) or waga(li, n, p+1)


print(waga(li, 9, 0))