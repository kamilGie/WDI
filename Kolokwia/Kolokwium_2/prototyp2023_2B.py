# ====================================================================================================>
# Zadanie 2B, 2024-01-04
# Na liczbach naturalnych możemy wykonywać następujące operacje:
# 1. 𝐴(𝑛) zamienia liczbę 𝑛 na sumę jej podzielników właściwych (mniejszych od samej liczby), np.
# 𝐴(1) = 1, 𝐴(6) = 6, 𝐴(12) = 16, 𝐴(17) = 1.
# 2. 𝐵(𝑛) zamienia liczbę 𝑛 na najmniejszy, większy od tej liczby wyraz ciągu Fibonacciego, np.
# 𝐵(1) = 2, 𝐵(4) = 5, 𝐵(8) = 13.
# 3. 𝐶(𝑛) zwiększa liczbę 𝑛 o liczbę będącą rewersem liczby 𝑛, np. 𝐶(1) = 2, 𝐶(10) = 11, 𝐶(13) = 44
# Proszę napisać funkcję cycle(x,n), która sprawdza czy startując od liczby 𝑥 możemy do niej powrócić
# wykonując sekwencję operacji spośród A,B,C o długości większej od 1 i nie większej od n. Jeżeli jest to
# możliwe, funkcja powinna zwrócić długość znalezionej sekwencji operacji, w przeciwnym wypadku
# należy zwrócić wartość 0.
# Na przykład wywołanie:
# cycle(29,6) powinno zwrócić 4 (cykl 29, B, 55, B, 89, C, 187, A, 29), [przykład jest błędny, 𝐵(29) = 34]
# cycle(31,6) powinno zwrócić 0.
# ====================================================================================================>


def Zadanie_2B(): ...


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_2B()
    # stworz_zadanie([Zadanie_2B])
