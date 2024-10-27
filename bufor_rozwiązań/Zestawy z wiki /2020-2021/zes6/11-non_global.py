def rek(t, il, left, i = 0, n = None, already_choosen = False, history = None, counter = 0):
    history = history or []
    n = n or len(t)

    if left == 0 or i == n:
        if left == 0 and il == 1 and already_choosen:
            print("FOUND:", history)
            return counter + 1
        return counter
    

    counter = rek(t, il, left, i+1, n, already_choosen, [*history], counter)

    if il % t[i] == 0:
        counter = rek(t, il//t[i], left-1, i+1, n, True, [*history, t[i]], counter)
    

    return counter


arr = [1,2,3,4,5,6]

from time import time
a = time()
print(rek(arr, 12, 3))

print(time()-a)