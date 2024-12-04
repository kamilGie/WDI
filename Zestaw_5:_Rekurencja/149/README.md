<picture>
  <source srcset="../../srt/zbior_zadan/149.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_149.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_149.png" alt="zadanie 149">
</picture>

```python

def suma_asci(napis):
    return sum(ord(ch) for ch in napis)


def kombinacje(litery, k):
    if k == 0:
        yield ""
        return
    if len(litery) < k:
        return

    # Kombinacje z pierwszą literą
    for comb in kombinacje(litery[1:], k - 1):
        yield litery[0] + comb

    # Kombinacje bez pierwszej litery
    yield from kombinacje(litery[1:], k)


def wyraz(s1, s2):
    samogloski = {"a", "e", "i", "o", "u", "y"}

    # Zbiór `s2` dzielę na dwa podzbiory: spółgłoski i samogłoski.
    samogloski_s2 = []
    spolgloski_s2 = []
    for ch in s2:
        if ch in samogloski:
            samogloski_s2.append(ch)
        else:
            spolgloski_s2.append(ch)

    # licze samogloski w s1
    liczba_samoglosek_s1 = 0
    for ch in s1:
        if ch in samogloski:
            liczba_samoglosek_s1 += 1

    # Z podzbioru samogłosek generuję napisy, które mają długość równą liczbie samogłosek w `s1`.
    for samogloskowy_napis in kombinacje(samogloski_s2, liczba_samoglosek_s1):
        wymagana_suma = suma_asci(s1) - suma_asci(samogloskowy_napis)

        # Następnie ze zbioru spółgłosek generuję napisy, i sprawdzam czy w sumie ASCII dają wymaganą wartość.
        for k in range(len(spolgloski_s2) + 1):
            for spolgloskowy_napis in kombinacje(spolgloski_s2, k):
                if suma_asci(spolgloskowy_napis) == wymagana_suma:
                    print(samogloskowy_napis + spolgloskowy_napis)
                    return True

    return False

```
