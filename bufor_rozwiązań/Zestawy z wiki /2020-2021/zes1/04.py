liczba = int(input())

suma = 0
el = 1
i = 0
while suma < liczba:
    suma += el
    i += 1
    if liczba == suma:
        print(i)
    elif suma > liczba:
        print(i-1)
        break
    el += 2
