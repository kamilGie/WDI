# Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.

def get_first_digit(num):
    while num > 9:
        num //= 10
    
    return num


def rek(x, y):
    if x == 7 and y == 7:
        return True
    
    global board

    try:
        cand = get_first_digit(board[y][x+1])
        if cand > board[y][x] % 10:
            if rek(x+1, y):
                return True
    except IndexError:
        pass
    
    try:
        cand = get_first_digit(board[y+1][x+1])
        if cand > board[y][x] % 10:
            if rek(x+1, y+1):
                return True
    except IndexError:
        pass
    
    try:
        cand = get_first_digit(board[y+1][x])
        if cand > board[y][x] % 10:
            if rek(x, y+1):
                return True
    except IndexError:
        pass
    

    return False
    



board = [
    [1,4,6,2,3,5,35,2],
    [1,4,6,2,3,5,35,2],
    [1,4,6,82,3,5,35,2],
    [1,4,6,2,3,5,35,2],
    [1,4,6,2,3,5,91,2],
    [1,4,6,82,3,5,24,2],
    [1,4,6,2,3,5,35,7],
    [1,4,6,2,3,5,35,8],
]

print(rek(0, 0))