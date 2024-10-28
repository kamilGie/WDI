# ====================================================================================================>
# Zadanie 14
# Dwie różne liczby nazywamy zaprzyjaźnionymi gdy każda jest równa sumie podzielników
# właściwych drugiej liczby, na przykład 220 i 284. Proszę napisać program wyszukujący liczby zaprzyjaźnione
# mniejsze od miliona.
# ====================================================================================================>
# kazda para w jednej linijce print((a,b))


def dzielniki(n):
    i = 2
    suma = 1
    while i * i < n:
        if n % i == 0:
            suma += i + (n // i)
        i += 1

    if i * i == n:
        suma += i

    return suma


def Zadanie_14():
    for num in range(2, 1000001):
        sum_divisors_num = dzielniki(num)

        if dzielniki(sum_divisors_num) == num and num > sum_divisors_num:
            print(num, sum_divisors_num)


