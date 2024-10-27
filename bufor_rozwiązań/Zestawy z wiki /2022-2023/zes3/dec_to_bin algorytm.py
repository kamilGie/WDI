def dec_to_bin(n):
    mult=1
    liczba=0
    while n > 0:
        liczba = liczba + mult * ( n%2 )
        mult = 10*mult
        n = n//2

    return liczba

n = int(input())
print( dec_to_bin(n) )
