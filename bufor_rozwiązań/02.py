# Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie,
# aby w ciągu analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku

suma=10000
best=(0,0)

for i in range(1,2023):
    x=i
    y=2022

    while x>0 and y>x:
        x,y=y-x,x

    if x+y<suma:
        best=(x,y)
        suma=x+y
#end for

print(suma, best)