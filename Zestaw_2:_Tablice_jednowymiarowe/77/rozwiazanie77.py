# ====================================================================================================>
# Zadanie 77
# Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
# podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
# ====================================================================================================>
# zwroc dlugosci


def czy_palindrom(T, poczatek, koniec):
    while poczatek < koniec:
        if not (T[poczatek] % 2 or T[koniec] % 2):
            return False
        elif T[poczatek] != T[koniec]:
            return False
        poczatek += 1
        koniec -= 1

    return True


def Zadanie_77(T: list):
    max_dlugosci = 0
    for i in range(len(T) - 1):
        if not T[i] % 2:
            continue

        indeks_konca = len(T) - 1

        while indeks_konca > i:
            if T[i] == T[indeks_konca]:
                if czy_palindrom(T, i, indeks_konca):
                    dlugosci = indeks_konca - i + 1
                    if dlugosci > max_dlugosci:
                        max_dlugosci = dlugosci
                    break
            indeks_konca -= 1
    return max_dlugosci


