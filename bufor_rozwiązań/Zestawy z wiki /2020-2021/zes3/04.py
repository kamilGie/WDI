# Zadanie 4.
# Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
import math


def calc_level(fact, tab):
    a, b = 1, fact

    # print(len(tab))
    
    for i in range(1, len(tab)):
        try:
            a *= 10
            tab[i] += a//b
            a %= b
            if a == 0:
                break
        except IndexError:
            print(i)
            exit()

def aproximate_e(n, prec = 1000):
    if n > 1000:
        prec = int((n**0.9)*1.2)
    # additional_multiplayer = int(math.log10(prec)) + 2
    additional_multiplayer = 1
    digits = [1] + [0]*int(n*additional_multiplayer+10)
    n += 1

    factorial = 1
    for i in range(1, prec):
        factorial *= i
        calc_level(factorial, digits)
    
    # print(digits)
    for i in range(-1, -len(digits), -1):
        digits[i-1] += digits[i]//10
        digits[i] %= 10
    
    return digits[:n]

n = int(input())


e = aproximate_e(n)
print(e[0], end='.')
print("".join(map(str, e[1:])))


with open("e_nasa.txt") as f:
    e_nasa = "".join(f.read().strip().split())

print("NASA leng:", len(e_nasa))
# print("NASA leng:", e_nasa)

# print(e_nasa[:n])

if "".join(map(str, e[1:])) != e_nasa[:n]:
    print("ŹLE")
    for i, e in enumerate(zip("".join(map(str, e[1:])), e_nasa[:n])):
        e_my, e_nasa = e[0], e[1]
        if e_my != e_nasa:
            print(i, ':\ne_my:', e_my, "\ne_nasa:", e_nasa)
            break
    