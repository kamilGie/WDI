# Zadanie 16. 
# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
# będących liczbami pierwszymi?
import random


def contains_only_primes(num):
    primes = {2,3,5,7}

    while num > 0:
        if num%10 not in primes:
            return False
        num //= 10
    return True


def ex16(tab):
    for row in tab:
        for elem in row:
            if contains_only_primes(elem):
                break
        else:
            return False
            
    return True


def print_tab(tab):
	for line in tab:
		print(line)
	print("--------------")


n = 3
tab = [[random.randint(2, 9) for _ in range(n)] for _ in range(n)]
print_tab(tab)
print(ex16(tab))