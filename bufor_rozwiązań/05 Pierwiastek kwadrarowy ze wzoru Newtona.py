# a(n+1) = ( S/an + an) * 0.5


s = float( input() )

a1 = 1
a2 = ( s/a1 + a1) * 0.5

while abs( a2 - a1 ) > 0.00001:
    a1 = a2
    a2 = ( s/a1 + a1 ) * 0.5

print( a2 )
