![Zadanie 11](../../srt/zbior_zadan/11.png)
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