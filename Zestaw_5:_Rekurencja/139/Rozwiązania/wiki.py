# ====================================================================================================>
# Zadanie 139
# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
# niż 2,3,5. Jedynka też jest taką liczbą. Proszę napisać funkcję rekurencyjną, wypisującą liczby znajdujące
# się w przedziale od 1 do N włącznie.
# ====================================================================================================>


def Zadanie_139(N):
    def mnozenie(liczba, ostatnie_mnozenie):
        """ Mnożymy  przez 2, 3 i 5, a w ten sposób otrzymujemy wszystkie liczby dwu-trzy-piątkowe. """
        if liczba > N:
            return

        print(liczba)

        # Jeśli liczba powstała z pomnożenia przez 5, aby uniknąć powtórzeń, mnożymy ją tylko przez 5.
        mnozenie(liczba * 5, 5)

        # Jeśli liczba powstała z pomnożenia przez 3, aby uniknąć powtórzeń, mnożymy ją tylko przez 3 i 5.
        if ostatnie_mnozenie <= 3:
            mnozenie(liczba * 3, 3)

        # Jeśli liczba powstała z pomnożenia przez 2, to możemy pomnożyć ją przez 2, 3 lub 5.
        if ostatnie_mnozenie <= 2:
            mnozenie(liczba * 2, 2)

    mnozenie(1, 1)
