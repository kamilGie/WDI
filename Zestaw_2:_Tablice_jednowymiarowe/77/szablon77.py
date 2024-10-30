# ====================================================================================================>
# Zadanie 77
# Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
# podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
# ====================================================================================================>
# zwroc dlugosci


def Zadanie_77(T: list): ...


if __name__ == "__main__":
    from testy77 import odpal_testy

    Zadanie_77(list(input("Podaj T: ")))

    # odpal_testy()
