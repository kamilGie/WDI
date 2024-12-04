# ====================================================================================================>
# Zadanie 171
# Dana jest funkcja rozwiązująca problem wież Hanoi:
# def hanoi(n,a,b,c):
# if n>0:
# hanoi(n-1,a,c,b)
# print(a,’->’,c)
# hanoi(n-1,b,a,c)
# - Usunąć rekurencję zastępując ją stosem,
# - Zaimplementować algorytm bez użycia stosu ani rekurencji (Wikipedia).
# ====================================================================================================>


def hanoi_stos(n, a="a", b="b", c="c"): ...


def hanoi_wikipedia(n, a="a", b="b", c="c"): ...


if __name__ == "__main__":
    from testy171 import odpal_testy

    hanoi_stos(int(input("Podaj n: ")))
    hanoi_wikipedia(int(input("Podaj n: ")))

    # odpal_testy()
