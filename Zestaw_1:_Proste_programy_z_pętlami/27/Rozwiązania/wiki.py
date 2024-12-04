# ====================================================================================================>
# Zadanie 27
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
# ====================================================================================================>
# kazda funkcja ma zwracac bool
# 11 -> palindron_dziesietny -> True
# 11 -> palindron_dwojkowy -> False


def palindron_dziesietny(n):
    temp = n
    rev = 0

    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return temp == rev


def palindron_dwojkowy(n):
    napis = ""
    while n > 0:
        napis += str(n % 2)
        n = n // 2

    return napis == napis[::-1]


