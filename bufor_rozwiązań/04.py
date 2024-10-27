#Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności 1+3+5+7...=n^2

liczba = int( input() )
suma=0
licznik=0
nieparzysta=1


while suma<=liczba:
    suma += nieparzysta
    nieparzysta+=2
    licznik+=1


print(licznik-1)