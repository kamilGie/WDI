num = input()

if num[:len(num)//2] == (num[(len(num)+1)//2:])[::-1]:
    print("to palindrom")
else:
    print("to nie palindrom")

bin_num = bin(int(num))[2:]
if bin_num[:len(bin_num)//2] == (bin_num[(len(bin_num)+1)//2:])[::-1]:
    print("to palidrom binarny")
else:
    print("to nie palindrom binarny")
