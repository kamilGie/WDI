![Zadanie 71](../../srt/zbior_zadan/71.png)
```python
def Zadanie_71(sequence):
    if len(sequence) <= 2:
        return (len(sequence), len(sequence))

    r = sequence[1] - sequence[0]
    max_leng_incr = 1
    max_leng_decr = 1
    leng = 2
    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i - 1] + r:
            leng += 1
        else:
            if r > 0:
                max_leng_incr = max(max_leng_incr, leng)
            else:
                max_leng_decr = max(max_leng_decr, leng)
            leng = 2
            r = sequence[i] - sequence[i - 1]

        if r > 0:
            max_leng_incr = max(max_leng_incr, leng)
        else:
            max_leng_decr = max(max_leng_decr, leng)

    return max_leng_incr, max_leng_decr



```