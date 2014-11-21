def primo(numero):
    for i in range(2,numero):
         if (numero%i)==0:
             return False
    return True

for n in range(999,0,-1):
    x=0
    if primo(n):
        enesimo = -1
        for valorIesimo in range( 0,int(round((len(str(n))/2))) ):
            a = str(n)
            if (a[valorIesimo] == a[enesimo]):
                x=1
            else:
                x=0
            enesimo = enesimo-1
    if (x==1):
        print n
        break
