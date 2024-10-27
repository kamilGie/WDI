# Dana jest liczba naturalna. Napisz funkcje, ktora sprawdza, czy jest mozliwe pociecie liczby N na kawalki, tak aby kazdy z kawalkow
# byl liczba pierwsza oraz liczba kawalkow tez byla liczba pierwsza. Funkcja powinna zwracac wartosc logiczna. 
# np. divide(2347) = True, divide(2255) = False, divide(273) = True, divide(22222) = True, divide(23673) = True, divide(21722) = False


def is_prime(x):
    pass


def divide(N):
    def rek(N,i=0,a=0,cnt=0):
        if i == len(N):
            return is_prime(cnt)
        else:
            a*=10
            a+=N%10
            if is_prime(a):
                return rek(N//10,i+1,0,cnt+1) or rek(N//10,i+1,a,cnt)
            return rek(N//10,i+1,a,cnt)
    return rek(N)

print(divide(N))