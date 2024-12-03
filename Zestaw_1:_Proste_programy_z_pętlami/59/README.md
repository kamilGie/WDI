<picture>
  <source srcset="../../srt/zbior_zadan/59.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_59.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_59.png" alt="zadanie 59">
</picture>

`rozwiazanie` **nie korzysta**  z tablic, krotek ani żadnych ułatwiających metod.
Użyłem jedynie:
- działań na liczbach,
- rekurencji,
- pętli
- importu `random`,
- funkcji `print`.

W folderze `Rozwiązania` znajdują się cztery inne rozwiązania, które nie ograniczają się wyłącznie do działań z zestawu 1. Zostały stworzone na szybko i nie skupiałem sie na nich  wiec najszybsza funkcja z tych rozwiązań działa w 43 sekund i na luzie można je dalej ulepszać

### Czasy rozwiązań:

<img width="1508" alt="Zrzut ekranu 2024-11-2 o 14 10 17" src="https://github.com/user-attachments/assets/9864293c-bc25-4a51-adb2-472cec0a5567">

```python

# test Millera-Rabina sprawdzajacy czy liczba jest pierwsza.
# Mozna tez napisac jakis deterministyczny test.
# lecz dla liczb narcystycznych test Millera-Rabina dziala z wielkim prawdopodobeistwiem


import random


def pow_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result


def isprime(n, k=15):
    if n == 1:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow_mod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


# potrzebna do logarytmu
import math


# kiedys zrobie dokladniejsza dokumentacje tego programu
def narcystyczne_pierwsze():
    # zeby nie potegowac za kazdym razem potegi bede trzymal w zmiene ktore beda przy kazdym dodaniu dlugosci mnozyc
    P_2 = 2
    P_3 = 3
    P_4 = 4
    P_5 = 5
    P_6 = 6
    P_7 = 7
    P_8 = 8
    P_9 = 9

    def sprawdz_liczbe(licznik_liczb_digita, s):
        # jesli jest podzielna przez te liczby to nawet nie warto isc dalej bo wiemy ze nie jest pierwsza
        if (
            s % 2 == 0
            or s % 3 == 0
            or s % 5 == 0
            or s % 7 == 0
            or s % 11 == 0
            or s % 13 == 0
            # jesli jej dlugosci nie odpowiada dlugosci liczb zer to tez mozemy isc dalej
            or math.floor(math.log10(s)) + 1 != length
        ):
            return False

        # tworzymy w notacj liczacej liczbe sum
        licznik_liczb_sumy = 0
        tmp = s
        while tmp > 0:
            tmp, d = divmod(tmp, 10)
            licznik_liczb_sumy += 100**d

        # sprawdzamy czy liczby w naszej notacji liczacej sa takie same i  s jest pierwsza mamy wynik
        if licznik_liczb_sumy != licznik_liczb_digita or not isprime(s):
            return False

        print(s, end=" ")
        return True

    # tworze kombinacje powtorzen od 0 do 10 dla dlugosci zer i zamist zwracac te dlugosci sprawdzaj
    # ich liczbe wystapien kazdej liczby w notacji |liczba dziewiatek|liczba osemek|i tak dalej do 0|...
    # oraz wynik tych wystapien liczb razy dlugosci ilosci zer jaki mamy
    def kombinacje_powtorzen_dziesiatki(r, start=0, licznik_liczb=0, s=0):
        if r == 0:
            return sprawdz_liczbe(licznik_liczb, s)
        else:
            znalezione = 0
            i = start

            if i == 0:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 0, licznik_liczb + 100**i, s)
                i += 1
            if i == 1:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 1, licznik_liczb + 100**i, s + 1)
                i += 1
            if i == 2:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 2, licznik_liczb + 100**i, s + P_2)
                i += 1
            if i == 3:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 3, licznik_liczb + 100**i, s + P_3)
                i += 1
            if i == 4:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 4, licznik_liczb + 100**i, s + P_4)
                i += 1
            if i == 5:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 5, licznik_liczb + 100**i, s + P_5)
                i += 1
            if i == 6:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 6, licznik_liczb + 100**i, s + P_6)
                i += 1
            if i == 7:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 7, licznik_liczb + 100**i, s + P_7)
                i += 1
            if i == 8:
                znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 8, licznik_liczb + 100**i, s + P_8)
                i += 1
            znalezione += kombinacje_powtorzen_dziesiatki( r - 1, 9, licznik_liczb + 100**i, s + P_9)

            return znalezione

    length = 1
    print("2", "3", "5", "7", end=" ")
    znalezione = 4
    while znalezione != 7:
        length += 1
        P_2 *= 2
        P_3 *= 3
        P_4 *= 4
        P_5 *= 5
        P_6 *= 6
        P_7 *= 7
        P_8 *= 8
        P_9 *= 9
        znalezione += kombinacje_powtorzen_dziesiatki(length)
    print()

```
