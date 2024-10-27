import math


num = int(input())

leng = math.floor(math.log10(num)) + 1


while num > 0:
    if num % 10 == leng:
        print("jest")
        break
    num //= 10
else:
    print("nie ma")
