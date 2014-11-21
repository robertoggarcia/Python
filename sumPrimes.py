def primo(numero):
    for i in range(2,numero):
         if (numero%i)==0:
             return False
    return True
suma=0
i=1
primos=0
while True:
    i+=1
    if primo(i):
        suma = i + suma
        primos+=1
    if primos==1001:
        break
    print "---suma"
    print suma
    print "---primos"
    print primos
    
print suma
