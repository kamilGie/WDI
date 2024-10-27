# Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
# czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego

def iloczyn(liczba):
    a,b=1,1
    while a*b<liczba:
        a,b=b,a+b

    return (a*b==liczba)


liczba = int( input() )
print( iloczyn(liczba) )
