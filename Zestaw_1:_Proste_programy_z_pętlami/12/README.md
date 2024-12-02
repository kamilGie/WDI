![Zadanie 12](../../srt/zbior_zadan/12.png)
```python
def Czynniki(liczba):
    czynnik = 2  # (*)
    while czynnik * czynnik <= liczba:
        while liczba % czynnik == 0:  # (****)
            print(czynnik, end=" ")
            liczba = liczba // czynnik  # (***)
        czynnik += 1  # (**)
    if liczba > 1:
        print(liczba)  # (*****)



```