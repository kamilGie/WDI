# ====================================================================================================>
# Zadanie 147
# Problem wież w Hanoi (treść oczywista)
# ====================================================================================================>


def tower_of_hanoi(n, A, B, C): ...


if __name__ == "__main__":
    from testy147 import odpal_testy

    tower_of_hanoi(int(input('Podaj n: ')), int(input('Podaj A: ')), int(input('Podaj B: ')), int(input('Podaj C: ')))

    # odpal_testy()
