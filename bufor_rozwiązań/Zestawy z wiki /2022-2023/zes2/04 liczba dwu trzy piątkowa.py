# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.

def L235(n):
    liczba=1
    licznik=0
    while liczba <= n:
        pom=liczba
        while pom <= n:
            pom2=pom
            while pom2 <= n:
                licznik+=1
                pom2*=5
            #end while
            pom*=3
        #end while
        liczba*=2
    #end while
    return licznik

n = int( input("> ") )
print( L235(n) )


