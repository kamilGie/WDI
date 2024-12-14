# ====================================================================================================>
# Zadanie 148
# Problem 8 hetmanów
# ====================================================================================================>
# Problem polega na znalezieniu liczby możliwych ustawień 8 hetmanów na szachownicy 8x8 w taki sposób,
# aby żadne dwa hetmany nie atakowały się nawzajem.
# Przykładowe rozwiązanie to ustawienie hetmanów wzdłuż głównej przekątnej szachownicy.


def hetmany():
    def rek(K, i):
        # Jeśli osiągnięto ósmy wiersz, znaleziono poprawne rozwiązanie
        if i == 8:
            return 1
        wynik = 0
        # Próbujemy ustawić hetmana w każdej kolumnie bieżącego wiersza
        for x in range(8):
            # Sprawdzamy, czy pozycja jest bezpieczna
            bezpieczna_pozycja = True
            for j in range(i):
                # Sprawdź, czy hetman w kolumnie `x` nie jest w tej samej kolumnie lub na tej samej przekątnej
                if K[j] == x or abs(K[j] - x) == i - j:
                    bezpieczna_pozycja = False
                    break

            if bezpieczna_pozycja:
                K[i] = x  # Ustawiamy hetmana
                wynik += rek(K, i + 1)  # Rekurencja na kolejny wiersz
        return wynik

    return rek([0] * 8, 0)  # Tablica K przechowuje kolumny, w których są hetmany


