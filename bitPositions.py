numero = input()
numeroBits = bin(int(numero[0]))
if (len(numeroBits)==0):
    print "vacio"
else:
    numeroBits = numeroBits[2:]
    p1 = numero[1]
    p2 = numero[2]
    if ( numeroBits[p1-1] == numeroBits[p2-1] ):
        print "true"
    else:
        print "false"
