from collections import defaultdict

def are_different_digits(a, b, base):
    digits_a = defaultdict(lambda: False)
    digits_b = defaultdict(lambda: False)
    
    while a > 0:
        digits_a[a%base] = True
        a //= base
    
    while b > 0:
        digits_b[b%base] = True
        b //= base
    
    # print(base)
    # print(digits_a)
    # print(digits_b)

    for key in digits_a.keys() | digits_b.keys():
        if digits_a[key] and digits_b[key]:
            return False
    
    return True


# print(are_different_digits(123, 3321, 10))


a, b = 123, 522

for i in range(2, 16+1):
    if are_different_digits(a, b, i):
        print(i)
        break