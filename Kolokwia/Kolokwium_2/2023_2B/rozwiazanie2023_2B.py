# ====================================================================================================>
# Zadanie 2B, 2024-01-04
# Na liczbach naturalnych możemy wykonywać następujące operacje:
# 1. 𝐴(𝑛) zamienia liczbę 𝑛 na sumę jej podzielników właściwych (mniejszych od samej liczby), np.
# 𝐴(1) = 1, 𝐴(6) = 6, 𝐴(12) = 16, 𝐴(17) = 1.
# 2. 𝐵(𝑛) zamienia liczbę 𝑛 na najmniejszy, większy od tej liczby wyraz ciągu Fibonacciego, np.
# 𝐵(1) = 2, 𝐵(4) = 5, 𝐵(8) = 13.
# 3. 𝐶(𝑛) zwiększa liczbę 𝑛 o liczbę będącą rewersem liczby 𝑛, np. 𝐶(1) = 2, 𝐶(10) = 11, 𝐶(13) = 44
# Proszę napisać funkcję cycle(x,n), która sprawdza czy startując od liczby 𝑥 możemy do niej powrócić
# wykonując sekwencję operacji spośród A,B,C o długości większej od 1 i nie większej od n. Jeżeli jest to
# możliwe, funkcja powinna zwrócić długość znalezionej sekwencji operacji, w przeciwnym wypadku
# należy zwrócić wartość 0.
# Na przykład wywołanie:
# cycle(29,6) powinno zwrócić 4 (cykl 29, B, 55, B, 89, C, 187, A, 29), [przykład jest błędny, 𝐵(29) = 34]
# cycle(31,6) powinno zwrócić 0.
# ====================================================================================================>


def f_a(x): # A(n), zwraca wynik > 0 dla x >= 2
    d = 1
    out = 0
    while d <= x//2:
        out += d if x%d == 0 else 0
        d += 1
    return out

def f_b(x): # B(n), zwraca wynik > 0 dla x >= 1
    a = 1
    b = 1
    while b <= x:
        a, b = b, a+b
    return b

def f_c(x): # C(n), zwraca wynik > 0 dla x >= 1
    n = x
    rev = 0
    while n > 0: # odwracamy liczbę
        rev *= 10
        rev += n%10
        n //= 10
    return rev + x

def cycle(x, n):
    def rek(num, rem): # number, remaining
        if x == num and rem != n: # war. końcowy - OK
            return 0
        if rem == 0: # war. końcowy - nie wyszło
            return -1
        
        out = rek(f_a(num), rem-1) # Jeśli którykolwiek blok zakończy się poprawnym wynikiem, funkcja się cofnie.
        if out != -1:
            return out+1
        out = rek(f_b(num), rem-1)
        if out != -1:
            return out+1
        out = rek(f_c(num), rem-1)
        if out != -1:
            return out+1 
        
        return -1 # Nie znaleźliśmy poprawnej zmiennej - ta gałąź rekurencji nie dała poprawnego wyniku
    
    val = rek(x, n)
    return 0 if val == -1 else val


