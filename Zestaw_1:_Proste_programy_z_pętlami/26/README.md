![Zadanie 26](../../srt/zbior_zadan/26.png)
```python
def ulamek(a, b, n):
    print(a // b, end="")
    if a % b != 0:
        print(".", end="")
        a = a % b
        while a > 0 and n > 0:
            a = a * 10
            print(a // b, end="")
            a = a % b
            n = n - 1

```