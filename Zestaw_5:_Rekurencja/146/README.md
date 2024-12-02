<picture>
  <source srcset="../../srt/zbior_zadan/146.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_146.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_146.png" alt="zadanie 146">
</picture>

```python
def wypisz_dzialanie(split):
    res = ""
    for el in split:
        if el == 0:
            break
        if res != "":
            res += "+"
        res += str(el)

    if "+" in res:
        print(res)


def number_split(num, j, split):

    if num == 0:
        wypisz_dzialanie(split)

    if j == 0:
        min = 1
    else:
        min = split[j - 1]

    for i in range(min, num + 1):
        split[j] = i
        number_split(num - i, j + 1, split)
        split[j] = 0


def Zadanie_146(liczba):
    number_split(liczba, 0, [0] * liczba)



```