# ====================================================================================================>
# Zadanie 3, 16 grudnia 2021
# Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnymi ¿1 odbywają się wyścigi wież.
# Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
# Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieza startuje z prawego
# górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w
# lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą
# wykonać ruch z jednego pola na drugie tylko wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę
# napisać funkcje,która dla danej tablicy zwraca numer wiezy, która wygra wyścig lub zero jeżeli wyścig będzie
# nierozstrzygnięty. Można założyć, ze podczas wyścigu wieże nie spotkają się na jednym polu
# ====================================================================================================>


def Zadanie_3(T): ...


if __name__ == "__main__":
    from testy_2021_3 import odpal_testy

    Zadanie_3([[3, 3, 3], [3, 1, 10], [5, 7, 11]])  # return 2

    # odpal_testy()
