# ====================================================================================================>
# Zadanie 119
# Dana jest tablica int t[N][N] wypełniona przypadkowymi wartościami. Proszę napisać
# funkcję, która dla zmiennej typu tablica zwraca numer wiersza w którym występuje najdłuższy spójny
# fragment złożony z liczb o tej samej wartości. W przypadku kilku fragmentów o tej samej długości należy
# zwrócić pozycję pierwszego z nich.
# ====================================================================================================>

# chyba cos takiego jeszcze bede to analizowac


def najdluzszy_fragment(t):
    max_len = 0  # Najdłuższy znaleziony fragment
    max_row = -1  # Numer wiersza z najdłuższym fragmentem

    for i in range(len(t)):
        current_value = None  # Aktualna wartość, która jest analizowana
        current_length = 0  # Długość bieżącego fragmentu
        max_current_len = 0  # Długość najdłuższego fragmentu w bieżącym wierszu

        # Przechodzimy przez wszystkie elementy w wierszu
        for j in range(len(t[i])):
            if t[i][j] == current_value:  # Jeśli wartość się powtarza
                current_length += 1  # Zwiększamy długość fragmentu
            else:
                current_value = t[i][j]  # Zmieniamy wartość
                current_length = 1  # Resetujemy długość fragmentu do 1

            # Jeśli bieżący fragment jest dłuższy, zapisujemy go
            if current_length > max_current_len:
                max_current_len = current_length

        if max_current_len > max_len:
            max_len = max_current_len
            max_row = i

    return max_row


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_119()
    # stworz_zadanie([Zadanie_119])
