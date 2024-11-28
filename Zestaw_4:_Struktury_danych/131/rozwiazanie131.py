# ====================================================================================================>
# Zadanie 131
# Liczby rzeczywiste są reprezentowane w postaci krotek(c,u), gdzie c jest częścią całkowitą
# liczby, a u jest liczbą całkowitą utworzoną z cyfr po przecinku. Na przykład krotka(6,23)reprezentuje liczbę
# 6.23. Proszę napisać następujące funkcje:
# • Dodającą dwie liczby,
# • Odejmującą dwie liczby,
# • Mnożącą dwie liczby.
# ====================================================================================================>
# c,u sa stringami aby moc zapisac np 0.05
# -1.2 to bedzie np ("-1","2")
# -0.3 to bedzie ("-0","3")


def dodaj(liczba1, liczba2):
    """
    1. Funkcja najpierw sprawdza, czy któraś z liczb jest ujemna:
        - Jeśli `liczba1` jest ujemna, przekazuje jej wartość (bez znaku "-") do funkcji `odejmij`, zamieniając kolejność argumentów.
        - Jeśli `liczba2` jest ujemna, przekazuje jej wartość (bez znaku "-") do funkcji `odejmij`.
        - W ten sposób unika się przypadków, w których trzeba dodawać liczby ujemne.

    2. Oblicza liczbę cyfr po przecinku dla dłuższej z dwóch części dziesiętnych i wyrównuje obie liczby, dopisując brakujące zera na końcu.

    3. Tworzy sumę dwóch liczb:
        - Części całkowite i dziesiętne są łączone w jeden ciąg znaków, a następnie zamieniane na liczbę całkowitą.
        - Wynik jest sumą tych dwóch liczb.

    4. Wynikowa suma jest rozdzielana na część całkowitą i dziesiętną:
        - Część całkowita to wszystko przed cyframi po przecinku.
        - Część dziesiętna to wszystko po przecinku, z usunięciem nadmiarowych zer na końcu.

    """

    c1, u1 = liczba1
    c2, u2 = liczba2

    # 1
    if c1[0] == "-": return odejmij(liczba2, (c1[1:], u1))
    if c2[0] == "-": return odejmij(liczba1, (c2[1:], u2))

    # 2
    cyfry_po_przecinku = max(len(u1), len(u2))
    u1, u2 = u1.ljust(cyfry_po_przecinku, "0"), u2.ljust(cyfry_po_przecinku, "0")

    # 3
    suma = str(int(c1 + u1) + int(c2 + u2))

    # 4
    czesc_calkowita = suma[:-cyfry_po_przecinku] or "0"
    czesc_dziesietna = suma[-cyfry_po_przecinku:].rstrip("0") or "0"

    return czesc_calkowita, czesc_dziesietna


def odejmij(liczba1, liczba2):
    """
    1. Funkcja najpierw sprawdza, czy którakolwiek z liczb jest ujemna:
        - Jeśli `liczba2` jest ujemna, zamienia znak na dodatni i wywołuje funkcję `dodaj`.
        - Jeśli `liczba1` jest ujemna, zamienia znak na dodatni i wywołuje funkcję `dodaj`,
          oznaczając wynik jako ujemny.

    2. Sprawdza, która liczba jest większa:
        - Jeśli `liczba1` jest mniejsza od `liczba2`, zamienia je miejscami i wywołuje `odejmij`,
          oznaczając wynik jako ujemny.

    3. Oblicza różnicę:
        - Wylicza liczbę cyfr po przecinku na podstawie dłuższej z dwóch części dziesiętnych.
        - Wyrównuje obie liczby, dopisując brakujące zera na końcu ich części dziesiętnych.
        - Tworzy różnicę poprzez odjęcie liczby `liczba2` od `liczba1` (po scaleniu części całkowitych
          i dziesiętnych w jeden ciąg znaków).

    4. Rozdziela wynik:
        - Część całkowita to wszystko przed cyframi po przecinku.
        - Część dziesiętna to wszystko po przecinku, z usunięciem nadmiarowych zer na końcu.
    """
    c1, u1 = liczba1
    c2, u2 = liczba2

    # 1
    if c2[0] == "-":
        return dodaj(liczba1, (c2[1:], u2))
    if c1[0] == "-":
        wynik_c, wynik_u = dodaj((c1[1:], u1), liczba2)
        return ("-" + wynik_c, wynik_u)

    # 2
    if (c1 < c2) or (c1 == c2 and u1 < u2):
        wynik_c, wynik_u = odejmij(liczba2, liczba1)
        return ("-" + wynik_c, wynik_u)

    # 3
    cyfry_po_przecinku = max(len(u1), len(u2))
    u1, u2 = u1.ljust(cyfry_po_przecinku, "0"), u2.ljust(cyfry_po_przecinku, "0")
    roznica = str(int(c1 + u1) - int(c2 + u2)).zfill(cyfry_po_przecinku + 1)

    # 4
    czesc_calkowita = roznica[:-cyfry_po_przecinku]
    czesc_dziesietna = roznica[-cyfry_po_przecinku:].rstrip("0") or "0"

    return czesc_calkowita, czesc_dziesietna


def pomnoz(liczba1, liczba2):
    """
    1. Określenie znaku wyniku:
        - Wynik jest ujemny, jeśli tylko jedna z liczb ma znak "-" w części całkowitej.
        - Jeśli obie liczby mają znak "-", wynik jest dodatni.

    2. Przygotowanie danych do obliczeń:
        - Usuwany jest znak "-" z części całkowitych obu liczb.
        - Liczba cyfr po przecinku jest sumą długości części dziesiętnych obu liczb.

    3. Obliczanie iloczynu:
        - Obie liczby są traktowane jako ciągi znaków połączone z ich części całkowitej i dziesiętnej.
        - Połączone liczby są mnożone jako liczby całkowite.

    4. Rozdzielenie wyniku:
        - Część całkowita wyniku to wszystko przed miejscem, gdzie zaczyna się część dziesiętna.
        - Część dziesiętna wyniku to wszystko po tym miejscu, z usunięciem nadmiarowych zer na końcu.
    """
    c1, u1 = liczba1
    c2, u2 = liczba2

    # 1
    znak =  "-" if (c1[0] == "-" or c2[0] == "-") and not (c1[0] == "-" and c2[0] == "-") else ""

    # 2
    c1, c2 = c1.lstrip("-"), c2.lstrip("-")
    cyfry_po_przecinku = len(u1) + len(u2)

    # 3
    iloczyn = str(int(c1 + u1) * int(c2 + u2)).zfill(cyfry_po_przecinku + 1)

    # 4
    czesc_calkowita = znak + iloczyn[:-cyfry_po_przecinku]
    czesc_dziesietna = iloczyn[-cyfry_po_przecinku:].rstrip("0") or "0"

    return czesc_calkowita, czesc_dziesietna


if __name__ == "__main__":
    from testy131 import odpal_testy

    # dodaj(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))
    # odejmij(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))
    # pomnoz(int(input("Podaj liczba1: ")), int(input("Podaj liczba2: ")))

    odpal_testy()
