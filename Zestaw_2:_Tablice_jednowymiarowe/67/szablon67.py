# ====================================================================================================>
# Zadanie 67
# Dana jest N-elementowa tablica T zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby T[k]. Napisać
# funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
# ====================================================================================================>
# return true jak moze lub false jak nie moze


def Zadanie_67(T) -> bool: ...


if __name__ == "__main__":
    from testy67 import odpal_testy

    Zadanie_67(int(input('Podaj T: ')))

    # odpal_testy()
