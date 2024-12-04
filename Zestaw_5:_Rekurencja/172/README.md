<picture>
  <source srcset="../../srt/zbior_zadan/172.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_172.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_172.png" alt="zadanie 172">
</picture>

```python
def fibonacci(n, a=0, b=1):
    return fibonacci(n - 1, b, a + b) if n > 0 else a
```

# Opis `fibonacci`
Rekurencyjna wersja obliczania ciągu Fibonacciego, która działa tak, jak pętla `for`, wykonując się, dopóki `n` jest większe niż 0. 

Funkcja przyjmuje dwa dodatkowe argumenty `a` i `b`, które reprezentują dwa elementy ciągu. Domyślne wartości `a=0` i `b=1` odpowiadają pierwszym dwóm wyrazom ciągu Fibonacciego. 

Funkcja rekurencyjnie wywołuje siebie, aż do osiągnięcia wartości `n`, zwracając końcowy wynik.






