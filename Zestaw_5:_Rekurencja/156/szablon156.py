# ====================================================================================================>
# Zadanie 156
# Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.
# ====================================================================================================>


def Zadanie_156(t, target): ...


if __name__ == "__main__":
    from testy156 import odpal_testy

    Zadanie_156(int(input('Podaj t: ')), int(input('Podaj target: ')))

    # odpal_testy()
