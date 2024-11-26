# ====================================================================================================>
# Zadanie 168
# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
# czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawał-
# ków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Naprzykład: divide(2347)=True,
# podział na 23 i 47, natomiast divide(2255)=False.
# Przykładowe wywołania funkcji:
# print(divide(273)) # True, podział 2|7|3
# print(divide(22222)) # True, podział 2|2|2|2|2
# print(divide(23672)) # True, podział 23|67|2
# print(divide(2222)) # False
# print(divide(21722)) # False
# ====================================================================================================>


def divide(N): ...


if __name__ == "__main__":
    from testy168 import odpal_testy

    divide(int(input('Podaj N: ')))

    # odpal_testy()
