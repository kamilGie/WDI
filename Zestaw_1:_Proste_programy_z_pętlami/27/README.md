![Zadanie 27](../../srt/zbior_zadan/27.png)
```python
def palindron_dziesietny(n):
    temp = n
    rev = 0

    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return temp == rev


def palindron_dwojkowy(n):
    napis = ""
    while n > 0:
        napis += str(n % 2)
        n = n // 2

    return napis == napis[::-1]



```