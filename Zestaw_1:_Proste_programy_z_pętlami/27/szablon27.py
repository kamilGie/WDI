# ====================================================================================================>
# Zadanie 27
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
# ====================================================================================================>
# kazda funkcja ma zwracac bool
# 11 -> palindron_dziesietny -> True
# 11 -> palindron_dwojkowy -> False


def palindron_dziesietny(n): ...


def palindron_dwojkowy(n): ...


if __name__ == "__main__":
    from testy27 import odpal_testy

    n = int(input("Podaj n: "))
    palindron_dziesietny(n)
    palindron_dwojkowy(n)

    # odpal_testy()
