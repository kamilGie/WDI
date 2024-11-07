# ====================================================================================================>
# Zadanie 19
# Dany jest ciąg określony wzorem: A =(A mod2)∗(3∗A +1)+(1−A mod2)∗A /2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
# wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.
# ====================================================================================================>
# return wyraz


def An1(A):
    """
    :param A: An
    :return: An+1

    Funckja zwraca wartość An+1 na podstawie An
    """
    return (A % 2) * (3 * A + 1) + (1 - A % 2) * A / 2


def Zadanie_19():
    # epsilon bo komputer nie umie w dzielenie i liczby sobie równo mogą sie rożnić na jakieś liczbie po przecinku
    eps = 1e-10
    # Dowolne małe num i maxi bo i tak zostaną nadpisane
    num = 2
    maxi = 1
    # Przechodzimy w pętli przez wszystkie liczby 2-10000 (+1 bo range nie wlicza ostatniej liczby)
    for i in range(2, 10000 + 1):
        A = i
        cnt = 0
        # Przechodzimy w pętli podstawiając kolejne elementy ciągu aż liczby bedą równe czyli aż różnica między nimi będzie mniejsza niż epsilon
        while abs(A - 1) > eps:
            A = An1(A)
            cnt += 1
        # Jeżeli liczba kroków jest większa od poprzedniej to ją zapisujemy i zapisujemy dla jakiej liczby to było
        if cnt > maxi:
            maxi = cnt
            num = i
    return num


