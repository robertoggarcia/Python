lista = "3 5 20".split()
maximo = int(list_[2])
result = ""

for i in range(1,maximo+1):
    if ((i%int(lista[0]))==0) and ((i%int(lista[1]))==0):
        result += str("FB ")
    elif (i%int(lista[0]))==0:
        result += str("F ")
    elif (i%int(lista[1]))==0:
        result += str("B ")
    else:
        result += str(i) + " "        
print result
