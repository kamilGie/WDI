# ====================================================================================================>
# Zadanie 3 2020
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi.
# Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
# „szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić położenie wież w postaci krotki (row ,col ,row ,col ).
# Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
# Przykładowe wywołania funkcji:
# print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
# print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35
# ====================================================================================================>
# chess(([[4,0,2],[3,0,0],[6,5,3]])) --> return(0,1,1,0)


def chess(tab): ...

if __name__ == "__main__":
    from testy114 import odpal_testy

    # chess(list(input("Podaj tab: ")))

    odpal_testy()
