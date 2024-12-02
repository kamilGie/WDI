# ====================================================================================================>
# Zadanie 124
# Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy
# struktury dane= [(x1 ,y1 ),(x2 ,y2 ),(x3 ,y3 ),...(xn ,yn )].
# Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty
# wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.
# ====================================================================================================>


def Zadanie_124(Struktura):
    najblizszy_osi = min(max(abs(x), abs(y)) for x, y in Struktura)
    return (
        najblizszy_osi != 0
        and (najblizszy_osi, najblizszy_osi) in Struktura
        and (najblizszy_osi, -najblizszy_osi) in Struktura
        and (-najblizszy_osi, najblizszy_osi) in Struktura
        and (-najblizszy_osi, -najblizszy_osi) in Struktura
    )
