
![black_Zrzut ekranu 2024-12-3 o 23 20 55](https://github.com/user-attachments/assets/9ff49247-0adc-4cc5-a144-a326d455c60b)

```python
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(6, int(num**0.5) + 3, 6):
        if num % (i + 1) == 0 or num % (i - 1) == 0:
            return False

    return True


def rek(num, nums, i, parts):
    # print(num, nums, i, parts)

    if is_prime(num) and is_prime(parts):
        return True

    if i > num:
        return False

    if is_prime(num % i):
        if rek(num // i, [num % i] + nums, 10, parts + 1):
            return True

    return rek(num, [*nums], i * 10, parts)


def divide(N):
    return rek(N, [], 10, 1)

```
