# ====================================================================================================>
# Zadanie 151
# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy
# króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
# liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
# obranego celu(np.narożnika) król nie może wykonaćl ruchu, który powoduje oddale niego od celu. Dana jest
# globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik
# ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do
# prawego dolnego narożnika.
# ====================================================================================================>
# return bool


def is_on_board(y, x, n):
    return x < n and y < n


def can_move_to(from_x, from_y, x, y):
    return from_x <= x and from_y <= y


def get_first(n):
    while n // 10 > 0:
        n = n // 10
    # end while
    return n % 10


def get_last(n):
    return n % 10


def Zadanie_151(tab, y, x):
    if y == 7 and x == 7:
        return True

    for i, j in [(1, 1), (1, 0), (0, 1)]:
        if can_move_to(y, x, y + i, x + j) and is_on_board(y + i, x + j, len(tab)):
            first = get_first(tab[y + i][x + j])
            last = get_last(tab[y][x])
            if last < first:
                return Zadanie_151(tab, x + i, y + j)

    return False


