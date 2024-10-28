"""
Warunki
1. W implementacjach można korzystać tylko z elementarnych konstrukcji Python'a
   (funkcje, instrukcje warunkowe, pętle, range). Nie wolno korzystać z tablic
   ani typu str.
2. Jeżeli temat wydaje się zbyt łatwy proszę założyć, że implementujemy program
   w języku Mini Python w którym typ int jest reprezentowany na dwóch bajtach
   (ma zakres -32768..32767).
3. Czas na rozwiązanie zadania 25 minut.

Zadanie 0 (Silnia)
Proszę napisać w języku Python program, który wyznacza ostatnia niezerową cyfra N! Program powinien
działać dla N rzędu 3000.
"""

# skrot notatki: rozwiazanie to jedna funkcja poprostu dodano tutaj 2 dodatkowe innym szybszym sposobem

# Notatki gologo:
# Zwróć uwagę na warunek 2.
# Lekko zmodyfikowałem oryginalne rozwiązania by wszystkie zmieścić w jednym
# pliku.
#
# I tak realistycznie rzecz biorąc - na faktycznym kolosie Garek by się
# najbardziej chyba ucieszył z pierwszego rozwiązania. Nie jest najwydajniejsze,
# ale nie jest też przesadnie wolne, a jest proste.
# Najłatwiejszą metodą na przejebanie WDI jest bawienie się w mikrooptymalizacje.
#   "Kod ma wyglądać, a nie działać"


def silnia(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        while factorial % 10 == 0:
            factorial //= 10
    return factorial % 10


def zad0better(num):
    digits = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

    # xddd
    if num < 10:
        return digits[num]

    ten_digit = (num // 10) % 10
    if ten_digit % 2 == 1:
        return 4 * zad0better(num // 5) * digits[num % 10] % 10
    else:
        return 6 * zad0better(num // 5) * digits[num % 10] % 10


def zad0iter(n):
    no_of_5 = 0
    power = 5
    while power <= n:
        no_of_5 += n // power
        power *= 5

    skip = no_of_5

    last_digit = 1
    for i in range(1, n + 1):
        # print(i)
        while i % 5 == 0:
            i //= 5
        if skip > 0 and i % 2 == 0:
            i //= 2
            skip -= 1
        # print(i)
        last_digit = (last_digit * i) % 10
    return last_digit
