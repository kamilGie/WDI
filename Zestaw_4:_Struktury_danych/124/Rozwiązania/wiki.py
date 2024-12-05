# ====================================================================================================>
# Zadanie 124
# Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy
# struktury dane= [(x1 ,y1 ),(x2 ,y2 ),(x3 ,y3 ),...(xn ,yn )].
# Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty
# wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.
# ====================================================================================================>


from math import inf


def Zadanie_124(Struktura):
    # Obliczanie najbliższego punktu od osi współrzędnych
    najblizszy_osi = inf
    for x, y in Struktura:
        odleglosc = max(abs(x), abs(y))  # Maksymalna odległość od osi dla tego punktu
        if odleglosc < najblizszy_osi:
            najblizszy_osi = odleglosc

    # Jeśli najbliższy punkt do osi to (0, 0), zwracamy False
    if najblizszy_osi == 0:
        return False

    # Sprawdzanie obecności czterech wymaganych punktów w strukturze
    prawa_gora = (najblizszy_osi, najblizszy_osi)
    prawa_dol = (najblizszy_osi, -najblizszy_osi)
    lewa_gora = (-najblizszy_osi, najblizszy_osi)
    lewa_dol = (-najblizszy_osi, -najblizszy_osi)

    # Sprawdzamy, czy wszystkie punkty są obecne w strukturze
    return ( prawa_gora in Struktura and prawa_dol in Struktura and lewa_gora in Struktura and lewa_dol in Struktura)
