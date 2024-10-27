def suma_num(num, n):
    suma = 0
    k = num
    while k > 0 :
        suma += ( k % 10 ) ** n
        k = k // 10
    #end while
    return suma==num

n = int( input() )
# liczba n cyfrowa zaczyna się od 10^(n-1) do 10^n - 1

for i in range( 10**(n-1), 10**n - 1):
    if suma_num(i, n): print( i )


