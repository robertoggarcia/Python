matriz = []
for renglon in range(3):
    matriz.append([])
    for columna in range(12):
        matriz[renglon].append( (columna+1)*(renglon+1) )
    print '%4d%4d%4d%4d%4d%4d%4d%4d%4d%4d%4d%4d'%(matriz[0][renglon],matriz[renglon][1],matriz[renglon][2],matriz[renglon][3],matriz[renglon][4],matriz[renglon][5],matriz[renglon][6],matriz[renglon][7],matriz[renglon][8],matriz[renglon][9],matriz[renglon][10],matriz[renglon][11])
