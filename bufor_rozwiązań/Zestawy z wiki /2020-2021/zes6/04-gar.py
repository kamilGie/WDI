from time import sleep
stop = False

def skoczek(t, w, k, p=1):
    global stop
    # tablica(t) to można dać żeby zobaczyć jak po kolei
    # sleep(0.5)  szuka rozwiązania
    if stop:
        return
    t[w][k] = p
    if p == len(t) ** 2:
        tablica(t)
        stop = True
    for i in range(8):
        x = check(t, w, k, i)
        if x is not None:
            skoczek(t, x[0], x[1], p + 1)
    t[w][k] = 0


def tablica(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()


def check(t, w, k, i):
    pion = [2, 1, -1, -2, -2, -1, 1, 2]
    poziom = [1, 2, 2, 1, -1, -2, -2, -1]
    new_w = w + pion[i]
    new_k = k + poziom[i]
    if 0 <= new_w < len(t) and 0 <= new_k < len(t) and t[new_w][new_k] == 0:
        return (new_w, new_k)
    return None



n = int(input())
tab = [[0 for _ in range(n)] for _ in range(n)]
skoczek(tab, 0, 0)