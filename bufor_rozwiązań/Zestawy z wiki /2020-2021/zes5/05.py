# Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
# [(x 1 , y 1 ), (x 2 , y 2 ), (x 3 , y 3 ), ...(x N , y N )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze ist-
# nieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.


# Punkty dodaj do set'u. Znajdź min_x, max_x, min_y, max_y. Dla każdego punktu (x, y) sprawdź czy istnieje taki punkt,
# że jego koordynaty to (x+i, y) dla pewnego i. Jeśli tak to sprawdź czy istnieje (x+i, y+j) dla pewnego j. 
# Jeśli tak to sprawdź czy istnieje (x, y+j). Jeśli tak to zwróć True, w przeciwnym wypadku False.
