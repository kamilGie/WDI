![black_Zrzut ekranu 2024-12-3 o 23 21 26](https://github.com/user-attachments/assets/a8c85af2-80d8-4c72-9d76-e2609c18e139)

```python
def f_a(x):  # A(n), zwraca wynik > 0 dla x >= 2
    d = 1
    out = 0
    while d <= x // 2:
        out += d if x % d == 0 else 0
        d += 1
    return out


def f_b(x):  # B(n), zwraca wynik > 0 dla x >= 1
    a = 1
    b = 1
    while b <= x:
        a, b = b, a + b
    return b


def f_c(x):  # C(n), zwraca wynik > 0 dla x >= 1
    n = x
    rev = 0
    while n > 0:  # odwracamy liczbę
        rev *= 10
        rev += n % 10
        n //= 10
    return rev + x


def cycle(x, n):
    def rek(num, rem):  # number, remaining
        if x == num and rem != n:  # war. końcowy - OK
            return 0
        if rem == 0:  # war. końcowy - nie wyszło
            return -1

        out = rek( f_a(num), rem - 1)  # Jeśli którykolwiek blok zakończy się poprawnym wynikiem, funkcja się cofnie.
        if out != -1:
            return out + 1
        out = rek(f_b(num), rem - 1)
        if out != -1:
            return out + 1
        out = rek(f_c(num), rem - 1)
        if out != -1:
            return out + 1

        return ( -1)  # Nie znaleźliśmy poprawnej zmiennej - ta gałąź rekurencji nie dała poprawnego wyniku

    val = rek(x, n)
    return 0 if val == -1 else val

```
