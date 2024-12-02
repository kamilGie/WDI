<picture>
  <source srcset="../../srt/zbior_zadan/11.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_11.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_11.png" alt="zadanie 11">
</picture>

```python
def divisors(n):
    if n == 0:
        print("Każda")
        return

    i = 1
    while i * i < n:
        if n % i == 0:
            print(i, n // i, end=" ")
        i += 1

    if i * i == n:
        print(i)



```