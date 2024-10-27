counter = 0

def rek(t, il, left, i = 0, n = None, already_choosen = False, history = []):
    n = n or len(t)

    # print(t, il, left, i, n)

    if left == 0 or i == n:
        if left == 0 and il == 1 and already_choosen:
            print("FOUND:", history)
            global counter
            counter += 1
        return il == 1
    

    rek(t, il, left, i+1, n, already_choosen, [*history])

    if il % t[i] == 0:
        rek(t, il//t[i], left-1, i+1, n, True, [*history, t[i]])



from time import time
a = time()
arr = [1,2,3,4,5,6]
rek(arr, 12, 3)
print(counter)

print(time()-a)