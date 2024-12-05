
![black_Zrzut ekranu 2024-12-3 o 23 21 18](https://github.com/user-attachments/assets/fb7d1dfb-17f5-4e70-a3bf-12d5552a4bef)

# Wizualizacja Rozwiązania

### algorytm szukania:

Przechodzimy przez oba lustra i sprawdzamy, czy ich obrót wyśle laser do końca.

<div align="center"> 
    <video src="https://github.com/user-attachments/assets/bdd8c0d3-ea93-4d61-8bf2-59e2d0e163e5" width="400" />
</div>




Kod do wizualizacji znajduje się w folderze "rozwiązania". Można zmieniać ogród, ale jego wymiary muszą wynosić 6x6.


# Rozwiązanie

```python

def check(T):
    vct = [1, 0]  # wektor ruchu
    n = len(T)
    x, y = 0, 0
    while True:
        if T[y][x] == "\\":  # odbicie 1
            if vct[0] == 0:
                vct[0] = vct[1]
                vct[1] = 0
            else:
                vct[1] = vct[0]
                vct[0] = 0
        if T[y][x] == "/":  # odbicie 2
            if vct[0] == 0:
                vct[0] -= vct[1]  # przeciwny znak
                vct[1] = 0
            else:
                vct[1] -= vct[0]  # przeciwny znak
                vct[0] = 0
        if y + vct[0] >= n or y + vct[0] < 0 or x + vct[1] >= n or x + vct[1] < 0:
            if vct == [1, 0] and (x, y) == (n - 1, n - 1):
                return True  # meta
            return False  # ściana
        y, x = y + vct[0], x + vct[1]  # wykonujemy ruch


def swap(c):  # zamiana
    return "/" if c == "\\" else "\\"


def Zadanie_2A(ogrod):  # i//n == wsp. y; i%n == wsp. x; y - wiersz; x - kolumna
    n = len(ogrod)
    ns = n**2
    for i in range(ns):
        if ogrod[i // n][i % n] in ["/", "\\"]:  # zawiera lustro
            for j in range(i + 1, ns):  # wszystkie lustra po indeksie i
                if ogrod[j // n][j % n] in ["/", "\\"]:  # zawiera lustro
                    pom = ogrod  # nast. linijki zamieniają i sprawdzają ogród
                    pom[i // n][i % n] = swap(ogrod[i // n][i % n])
                    pom[j // n][j % n] = swap(ogrod[j // n][j % n])
                    if check(pom):
                        return pom
                    pom[i // n][i % n] = swap(
                        ogrod[i // n][i % n]
                    )  # powrót do stanu oryginalnego jeśli się nie udało
                    pom[j // n][j % n] = swap(ogrod[j // n][j % n])
    return None  # nie istnieje taka kombinacja

# Autor rozwiązania Piotr Polański

```
