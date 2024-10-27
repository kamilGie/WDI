def liczba_samoglosek(s):
    counter = 0
    n = len( s )
    for i in range( n ):
        if czy_samogloska( s[i] ): counter += 1
    #end for
    return counter


def czy_samogloska(z):
    elements = {'a', 'e', 'i', 'o', 'u', 'y'}
    if z in elements:
        return True
    #end if
    return False


def waga_wyrazu(s):
    suma = 0
    n = len(s)
    for i in range( n ):
        suma += ord( s[i] )
    #end for
    return suma



def zad16(s, T):  # s - wyraz, T - zbiór znaków
    def rek(s, x, T):
        if waga_wyrazu(x) > waga_wyrazu(s):
            return False

        if waga_wyrazu(x) == waga_wyrazu(s):
            if liczba_samoglosek(x) == liczba_samoglosek(s):
                print(x)
                return True

        for z in T:
            if rek(s, x + z, T):
                return True

        return False

    zad16(s, ['u', 'l', 'a'] )


