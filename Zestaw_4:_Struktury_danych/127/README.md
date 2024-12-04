<picture>
  <source srcset="../../srt/zbior_zadan/127.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_127.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_127.png" alt="zadanie 127">
</picture>

```python
def multi(T):
    res = 0 
    for napis in T:
        n = len(napis)

        # Przeszukiwanie od połowy długości napisu w dół
        for i in range(n // 2, 0, -1):
            # Sprawdzenie, czy długość napisu jest podzielna przez i
            if n % i == 0:
                # Sprawdzenie, czy podnapis powtarzany (n // i) razy jest równy oryginalnemu napisowi
                if napis[:i] * (n // i) == napis:
                    res = max(res, i)
                    break
    return res
```

# Opis Rozwiązania:
## `mulit`
Dla kazdego napisu iterujemy od połowy długości napisu w dół.

W każdej iteracji tworzę podnapis od 0 do bieżącej pozycji iteracji, sprawdzam, czy powtarzając podnapis , otrzymam oryginalny napis.

np dla:
1. `napis == "xyzxyzxyz"`
2. `n == 9`
3. `i == 4` bo jest polowa n zaokregolona w dol 
4. n nie jest podzielne przez i ide dalej
5. `i == 3`
6. `napis[:i] == "xyz"`
7. `napis[:i] * (n // i) == "xyzxyzxyz"`
8. powtorzenie podnapisu daje orginalny napis mam napis wielokrotny dlugosci
