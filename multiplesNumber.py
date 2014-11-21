entrada = input()
x=entrada[0]
n=entrada[1]
bandera=True
multiplo=1
while bandera:
    if ( multiplo*(1/n)==0 and multiplo>x):
        print multiplo
        bandera = False
        break
    multiplo += 1
