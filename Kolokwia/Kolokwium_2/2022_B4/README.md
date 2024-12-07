
![black_Zrzut ekranu 2024-12-6 o 11 18 07](https://github.com/user-attachments/assets/dace54b2-b630-431f-a13d-52133f1359fb)

```python

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
# Opis Rozwiązania

# Wizualizacja algorytmu

<div align="center">
  <video src="https://github.com/user-attachments/assets/d2717368-5ad3-42b4-94a6-d5a1232d8dbb" width="400" />
</div>

> **Wydajność:**
> Można zauważyć, że jest to nieoptymalne rozwiązanie. Lepszym podejściem byłoby znalezienie 
> jednego nieszachowanego pola i wstawianie kolejno każdej wieży – jedna z nich na pewno będzie 
> rozwiązaniem, niezależnie od tego, które nieszachowane pole wybierzemy. 
> Jednak dla prostoty rozwiązań z kolokwiów zdecydowałem się dodać najprostsze rozwiązanie.

