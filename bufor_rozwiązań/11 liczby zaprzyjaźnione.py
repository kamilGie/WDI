def dzielniki(n):
    i=2
    suma=1
    while i*i < n:
        if n % i == 0:
            suma += i + (n//i)
        #end if
        i+=1
    #end while

    if i*i == n: suma+=i

    return suma


for num in range(2, 1000001):
    sum_divisors_num = dzielniki( num )

    if dzielniki( sum_divisors_num ) == num and num > sum_divisors_num:
        print(num, sum_divisors_num)