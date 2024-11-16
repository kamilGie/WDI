# ====================================================================================================>
# Zadanie 146
# Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę skład-
# ników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
# ====================================================================================================>


def wypisz_dzialanie(split):
    res = ""
    for el in split:
        if el == 0:
            break
        if res != "":
            res += "+"
        res += str(el)

    if "+" in res:
        print(res)


def number_split(num, j, split):

    if num == 0:
        wypisz_dzialanie(split)

    if j == 0:
        min = 1
    else:
        min = split[j - 1]

    for i in range(min, num + 1):
        split[j] = i
        number_split(num - i, j + 1, split)
        split[j] = 0


def Zadanie_146(liczba):
    number_split(liczba, 0, [0] * liczba)


