# Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
# o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
# która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
# -1.


def div(num):
    i = 2
    c_num = num
    arr = []
    while num > 1 and i < c_num:
        if num % i == 0:
            arr.append(i)
            while num % i == 0:
                num //= i
        i += 1
    
    return arr


def rek(t, index = 0, jumps = 0):
    if index >= len(t)-1:
        if index == len(t)-1:
            return jumps
        return -1

    divs = div(t[index])

    for divisor in divs:
        res = rek(t, index+divisor, jumps+1)
        if res >= 0:
            return res
    
    return -1

arr = [4,4,6,1,1,3,1]

print(rek(arr))