def to_system(num , base):
    base_num = []
    chars = [str(i) for i in range(10)] + [chr(i) for i in range(ord("A"), ord("F")+1)]
    # print(chars)

    while num > 0:
        base_num.append(chars[num%base])
        num //= base
    
    return "".join(base_num[::-1])


n = int(input())

for i in range(2, 16+1):
    print("base", i, ":", to_system(n, i))