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

for i in range(1,1000001):
    if i==dzielniki(i): print(i, end=" ; ")
