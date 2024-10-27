# Punkty dodaj do set'u. Znajdź min_x, max_x, min_y, max_y. Dla każdego punktu (x, y) sprawdź czy istnieje taki punkt,
# że jego koordynaty to (x+i, y) dla pewnego i. Jeśli tak to sprawdź czy istnieje (x+i, y+j) dla pewnego j.
# Jeśli tak to sprawdź czy istnieje (x, y+j). Jeśli tak to zwróć True, w przeciwnym wypadku False.

def kwadrat(dane):
    n = len(dane)
    tab_x = [] * n
    tab_y = [] * n

    for i in range(n):
        x, y = dane[i]
        tab_x[i] = x
        tab_y[i] = y

    min_x = tab_x[0]
    max_x = tab_x[n-1]

    min_y = tab_y[0]
    max_y = tab_y[n-1]

    tab_x=set(tab_x)
    tab_y=set(tab_y)

    for element in dane:
        x, y = element

        for i in range(x,max_y+1):
            if (x+i, y) in dane:
                for j in range(y+1,y+i+1):
                    if (x,j) in dane:
                        pass





