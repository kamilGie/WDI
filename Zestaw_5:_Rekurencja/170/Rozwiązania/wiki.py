# ====================================================================================================>
# Zadanie 170
# Dana jest funkcja Ackermana, określona na zbiorze liczb całkowitych nieujemnych, dana
# wzorem rekurencyjnym:
# def f(a,b):
#    if a==0: return b+1
#    if b==0: return f(a-1,1)
#    return f (a-1,f(a,b-1))
# Proszę napisać funkcję w wersji iteracyjnej.
# ====================================================================================================>


def Zadanie_170(a, b):
    """
    Kolejkowanie wywołań, będziemy tworzyć tablice `stos` która ma na ostanich 2 wartościach `a` i `b`.
    Wywołania są symulowane iteracyjnie poprzez odpowiednie manipulowanie stosu, aż do osiągnięcia końcowego wyniku.

    Stos początkowo zawiera dwie wartości: `a` i `b`.
    W każdej iteracji pobierane są dwie ostatnie wartości ze stosu.
    Na podstawie wartości `a` i `b` wyznaczane są nowe wartości
    i odkładane na stos, zgodnie z definicją funkcji Ackermanna:

    Proces trwa, dopóki na stosie nie zostanie tylko jedna wartość.
    """
    stos = [a, b]

    while len(stos) > 1:
        b, a = stos.pop(), stos.pop()

        if a == 0:
            stos.append(b + 1)
        elif b == 0:
            stos.append(a - 1)
            stos.append(1)
        else:
            stos.append(a - 1)
            stos.append(a)
            stos.append(b - 1)

    return stos[0]
