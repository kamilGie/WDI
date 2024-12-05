<picture>
  <source srcset="../../srt/zbior_zadan/118.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_118.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_118.png" alt="zadanie 118">
</picture>

```python
def Zadanie_118(T, w):
    n = len(w)
    res = (0, 0)
    max_nie_szachowanych = 0
    for w1 in range(n):
        for w2 in range(w1 + 1, n):
            nie_szachowane = T[w[w1]][w2] + T[w[w2]][w1]
            if nie_szachowane > max_nie_szachowanych:
                max_nie_szachowanych = nie_szachowane
                res = (w1, w2)

    return res
```
# Opis Rozwiązania:

Po usunięciu dwóch wież cztery pola stają się nieschowane, ale na dwóch z nich wcześniej stały wieże, więc i tak nie były szachowane. Jedynymi polami, które przestają być szachowane, są przecięcia, więc należy znaleźć maksymalne z tych przecięć.

<div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/5061a29d-f6b5-4b29-a7f4-3c56a153266e" style="width: 45%; height: auto;">
    <img src="https://github.com/user-attachments/assets/68d3df5a-5610-4fc9-9e45-b79141295649" style="width: 45%; height: auto;">
</div>

https://github.com/user-attachments/assets/8dd264d1-7c8e-4baf-803f-7d7dc0e0574c

program Wizualizacji w rozwiązaniach pod nazwa `pomoc_szachowania` można sie pobawić


