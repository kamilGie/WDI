from math import sqrt

liczba = int(input())
a1,a2=1,1

while a1 < sqrt(liczba)+1:
    if liczba % a1 == 0:
        b1,b2=a1,a2

        while a1*b1 < liczba:
            b1,b2=b2,b1+b2
        #end while

        if a1*b1 == liczba:
            print("Tak: ", (a1,b1) )
            break
        #end if 2
    #end if 1
    a1, a2 = a2, a1+a2

else: print("Nie")











