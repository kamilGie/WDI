def common_digit(a,b,s):
    tab = [False for _ in range(s)]

    while a != 0:
        tab[ a % s ] = True
        a = a // s
    #end while

    while b != 0:
        if tab[b % s] : return False
        b = b // s
    #end while
    return True

# --- main
a = int( input() )
b = int( input() )

for s in range(2, 17):
    if common_digit(a, b, s):
        print(s)
        break
    #end if
#end for
else: print("Nie ma takiego systemu")


