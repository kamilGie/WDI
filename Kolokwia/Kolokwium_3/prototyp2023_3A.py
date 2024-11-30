# ====================================================================================================>
# Zadanie 3A, 2024-01-18
# Dany jest ciąg 𝑁 liczb naturalnych, z których wybieramy spójny fragment o długości 𝐾 (1 < 𝐾 < 𝑁).
# Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania albo
# mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić
# dwa jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który
# pozwala zbudować wyrażenie o wartości będącej liczbą pierwszą, taką że stosunek tej liczby pierwszej
# do długości znalezionego fragmentu jest największy. Proszę napisać funkcję find_max(T), która dla
# ciągu zawartego w tablicy T, wyznaczy wartość maksymalnego ilorazu jaki można znaleźć. Jeżeli taki
# podciąg nie istnieje funkcja powinna zwrócić wartość zero.
# Na przykład dla ciągu: 7, 8, 6, 4, 7, 3 funkcja powinna zwrócić wartość 16.6.
# Możliwe podciągi dające liczby pierwsze to:
# 7 + 8 ⋅ 6 + 4 = 59, 59/4 = 14.75
# 7 + 8 ⋅ 6 + 4 ∗ 7 = 83, 83/5 = 16.6
# 6 ⋅ 4 + 7 = 31, 31/3 = 10.(3)
# 4 + 7 = 11, 11/2 = 5.5
# ====================================================================================================>


def Zadanie_3A(): ...


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_3A()
    # stworz_zadanie([Zadanie_3A])
