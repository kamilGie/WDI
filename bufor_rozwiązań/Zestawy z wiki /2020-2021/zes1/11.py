def sumOfDiv(num):
    s = 1
    i = 2
    while i**2 < num:
        if num % i == 0:
            s += i
            s += num//i
        i += 1
    if i**2 == num:
        s += i
    
    return s


if __name__ == "__main__":
    for num1 in range(2, 1_000_000):
        num2 = sumOfDiv(num1)
        if num1 > num2 and sumOfDiv(num2) == num1:
            print(num1, "i", num2, sep=" ")
