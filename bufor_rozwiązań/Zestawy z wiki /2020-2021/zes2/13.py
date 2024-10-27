# Zadanie 13.
# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba zakończona jest unikalną cyfrą.

def last_digit_unique(num):
    last_digit = num % 10
    num //= 10
    while num > 0:
        if num % 10 == last_digit:
            return False
        num //= 10
    return True


n = int(input())
print(last_digit_unique(n))