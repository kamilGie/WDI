<picture>
  <source srcset="../../srt/zbior_zadan/2022_B4.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2022_B4.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2022_B4.png" alt="zadanie 2022_B4">
</picture>

```python
# Brutal force, ale działa – najprościej


def wszystkie_szachowane(T):
    """Sprawdza, czy wszystkie pola na szachownicy T są szachowane."""
    # Tworzę tablicę szachowania przechowującą, czy pole jest szachowane.
    N = len(T)
    szachowane = []
    for i in range(N):
        szachowane.append([False] * N)

    # Sprawdź, które pola są szachowane przez wieże.
    for i in range(N):
        for j in range(N):
            if T[i][j]:  # Jeśli jest wieża w tym miejscu.
                for k in range(N):
                    szachowane[i][k] = True  # Cały wiersz.
                    szachowane[k][j] = True  # Cała kolumna.

    # Sprawdź, czy wszystkie pola są szachowane.
    for i in range(N):
        for j in range(N):
            if not szachowane[i][j]:  # Jeśli pole nie jest szachowane.
                return False
    return True


def move(T):
    N = len(T)
    # Szukamy wież, aby je przestawić.
    for i in range(N):
        for j in range(N):
            if T[i][j]:  # Znalaziono wieżę.
                T[i][j] = False
                # Dla każdego pola sprawdzam, czy przeniesienie jej tam daje wszedzie szach
                for k in range(N):
                    for z in range(N):
                        if not T[k][z]:
                            T[k][z] = True
                            if wszystkie_szachowane(T):
                                return ((i, j), (k, z))
                            T[k][z] = False
                T[i][j] = True
    return
```
