<img width="794" alt="Zrzut ekranu 2024-12-2 o 01 23 48" src="https://github.com/user-attachments/assets/e393cb7e-f887-4973-b121-07579a08b174">
<img width="790" alt="Zrzut ekranu 2024-12-2 o 01 24 14" src="https://github.com/user-attachments/assets/8d186457-5e81-495a-aca5-4260a86f93ea">

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