![Zadanie 84](../../srt/zbior_zadan/84.png)
```python
def multi(T):
    """
    Dla kazdego napisu iterujemy od połowy długości napisu w dół.
    W każdej iteracji tworzę podnapis od 0 do bieżącej pozycji iteracji,
    sprawdzam, czy powtarzając podnapis , otrzymam oryginalny napis.
    """
    res = 0
    for napis in T:
        n = len(napis)
        for i in range(n // 2, 0, -1):
            if n % i == 0 and napis[:i] * (n // i) == napis:
                res = max(res, i)
                break
    return res

```