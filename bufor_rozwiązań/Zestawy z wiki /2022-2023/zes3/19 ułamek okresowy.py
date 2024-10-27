def skroc_ulamek(l, m):
    temp1, temp2= l, m
    while m > 0:
        l, m= m, l % m
    #end while

    return temp1 // l, temp2 // l

def il25(m):
    pom = m
    i = 2
    counter_2, counter_5 = 0, 0

    while pom % 2 == 0:
        counter_2 += 1
        pom = pom // 2
    #end while 1

    while pom % 5 == 0:
        counter_5 += 1
        pom = pom // 5
    #end while 2

    if counter_2 >= counter_5: return counter_2
    else: return counter_5
# Ilosc miejsc po przecinku bez okresu to max( ilosc dwojek, ilosc piatek w rozkladzie na czynniki pierwsze)

def ulamek(l, m):
    l, m = skroc_ulamek(l, m)
    print( l // m, end="")
    l = l % m
    if l > 0:
        print(".", end="")
        for _ in range( il25(m) ):
            l *= 10
            print( l//m, end="")
            l = l % m
        #end for
        if l > 0:
            print("(", end="")
            mem = l
            while True:
                l *= 10
                print( l//m, end="")
                l = l % m
                if l == mem: break
            #end while
            print(")", end="")
        #end if
    print()


# -------- main:

l = int( input() )
m = int( input() )
ulamek(l, m)
