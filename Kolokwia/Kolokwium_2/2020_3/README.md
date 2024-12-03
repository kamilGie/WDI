<img width="793" alt="Zrzut ekranu 2024-12-2 o 01 23 03" src="https://github.com/user-attachments/assets/da72dab8-3084-4219-9789-9861a484b776">
<img width="792" alt="Zrzut ekranu 2024-12-2 o 01 23 11" src="https://github.com/user-attachments/assets/91af08e6-fbff-48b5-b533-1a1856fffc38">

```python
import copy


def chess(tab):
    n = len(tab)
    best = float("-inf")
    best_positions = None

    for x in range(n):
        for y in range(n):

            suma_1 = 0
            tablica_z_wieza = copy.deepcopy(tab)
            tablica_z_wieza[x][y] = 0
            for x1 in range(0, n):
                suma_1 += tablica_z_wieza[x1][y]
                tablica_z_wieza[x1][y] = 0

            for y1 in range(0, n):
                suma_1 += tablica_z_wieza[x][y1]
                tablica_z_wieza[x][y1] = 0

            for a in range(x, n):
                for b in range(0, n):
                    if a == x and b == y:
                        continue
                    elif a == x or b == y:
                        suma_2 = -tab[a][b]
                    else:
                        suma_2 = 0

                    tablica_z_wieza[a][b] = 0

                    for a1 in range(0, n):
                        suma_2 += tablica_z_wieza[a1][b]

                    for b1 in range(0, n):
                        suma_2 += tablica_z_wieza[a][b1]

                    if suma_1 + suma_2 > best:
                        best = suma_2 + suma_1
                        best_positions = (x, y, a, b)

    return best_positions



```