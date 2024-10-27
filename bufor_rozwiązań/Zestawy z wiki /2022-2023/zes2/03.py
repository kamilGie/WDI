### GENIALNE !!!!!!!!!!!!!!!!!!!!!

def palindron(n):
    temp = n
    rev = 0

    while n > 0:
        dig = n % 10
        rev = rev*10 + dig
        n = n // 10
    #end while
    return temp == rev


### GENIALNE !!!!!!!!!!!!!!!!!!!!


def dec_to_bin_palindrom(n):
    napis=""
    while n>=1:
        napis+=str(n%2)
        n=n//2

    if napis==napis[::-1]:
        return "Liczba jest palindromem w systemie dwójkowym"

    else:
        return "Liczba nie jest palindromem w systemie dwójkowym"



n = int(input() )
print( palindron(n) )

# a1 = input()
#
# if a1==a1[::-1]: print("Liczba jest palindromem w systemie dzięsiętnym")
# else: print("Liczba nie jest palindromem w systemie dzięsiętnym")
#
# print( dec_to_bin_palindrom( int(a1) ) )


