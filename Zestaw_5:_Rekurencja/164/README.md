<picture>
  <source srcset="../../srt/zbior_zadan/164.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_164.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_164.png" alt="zadanie 164">
</picture>

```python
def Zadanie_164(num):
    def divisiors(num):
        div = []
        i = 2

        while num > 1:
            if num % i == 0:
                div.append(i)

                while num % i == 0:
                    num //= i
            i += 1

        print(div, end=" ")
        return div

    def rek(t, curr_i=0, il=1):
        if curr_i == len(t):
            if il == 1:
                return
            nonlocal s
            s += il
            return

        rek(t, curr_i + 1, il)
        rek(t, curr_i + 1, il * t[curr_i])

    s = 0

    rek(divisiors(num))

    print(s)



```