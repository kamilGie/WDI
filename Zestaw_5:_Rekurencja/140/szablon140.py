# ====================================================================================================>
# Zadanie 140
# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
# odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# ====================================================================================================>
# return bool


def Zadanie_140(T, okreslona_masa): ...


if __name__ == "__main__":
    from testy140 import odpal_testy

    Zadanie_140(int(input('Podaj T: ')), int(input('Podaj okreslona_masa: ')))

    # odpal_testy()
