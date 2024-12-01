# ====================================================================================================>
# Zadanie 53
# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
# niż 2,3,5. Jedynka też jest taką liczbą. Proszę napisać program, który wylicza ile takich liczb znajduje się w
# przedziale od 1 do N włącznie.
# ====================================================================================================>


def is_two_three_five(num):
    for div in {2, 3, 5}:
        while num % div == 0:
            num //= div
    return num == 1


def Zadanie_53(n):
    counter = 0
    for i in range(1, n + 1):
        if is_two_three_five(i):
            counter += 1

    return counter


