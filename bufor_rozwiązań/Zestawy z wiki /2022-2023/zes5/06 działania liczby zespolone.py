
def wczytywanie():
    re = int( input("Re >: ") )
    im = int( input("Im >: ") )

    return re, im


def wyp(c1):
    napis = str( c1[0] ) + " + " + str( c1[1] )+"i"
    print( napis )


def dodawanie(c1,c2):
    return c1[0] + c2[0], c2[1] + c2[1]



def odejmowanie(c1,c2):
    return c1[0] - c2[0], c2[1] - c2[1]



def mnozenie(c1,c2):
    return c1[0]*c2[0] - c1[1]*c2[1], c1[0]*c2[1] + c1[1]*c2[0]



def dzielenie(c1,c2):
    x, y = mnozenie(c1,c2)
    return x / ( c2[0] + c2[1] ), y / ( c2[0] + c2[1] )


def potegowanie(c1, n):
    z = complex(c1[0], c1[1])
    return z**n










