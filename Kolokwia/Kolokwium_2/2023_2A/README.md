<img width="795" alt="Zrzut ekranu 2024-12-1 o 14 22 37" src="https://github.com/user-attachments/assets/42ae33cd-3f14-4afe-a832-b9162852b862">

```python
# OPIS METODY
# funkcja obraca każde 2 możliwe lustra.
# potem iteruje przez tablicę i sprawdza, czy działa.


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