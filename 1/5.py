# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2

n = int(input("wprowadz liczbe do spierwiastkowania calkowicie"))

suma = 0
licznik = 0
while suma + (licznik + 1) * 2 - 1 <= n:
    licznik += 1
    suma += licznik * 2 - 1

print(int(licznik))
