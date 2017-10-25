import numpy as np
from random import randint

def kFoldCrossValidation(matriz, k):
    result = []
    lineSize = len(matriz)
    columnSize = len(matriz[0])
    indexer = {}
    indexerData = {}

    #inicializa as listas com k
    for x in range(0,k):
        result.append([])

    #Corre todas as linhas e adiciona quantidade de itens por classe
    for i in range(0,lineSize):
        if matriz[i][columnSize-1] in indexer:
            indexer[matriz[i][columnSize-1]]=indexer[matriz[i][columnSize-1]]+1
            indexerData[matriz[i][columnSize - 1]].append(matriz[i])
        else:
            indexer[matriz[i][columnSize - 1]] = 1
            indexerData[matriz[i][columnSize - 1]] = [matriz[i]]

    #Corre classe por classe
    for key,val in indexer.items():
        #Pega a quantidade media dessa classe por grupo
        partsPerK = val / k;

        #Corre odos os Ks
        for i in range(0,k):
            #Popula cada k preenchendo a quantidade partsPerK de uma classe
            for e in range(0,partsPerK):
                drawn = randint(0,len(indexerData[key])-1)
                currentItem = indexerData[key][drawn]
                result[i].append(currentItem)
                indexerData[key].remove(currentItem)

    #Popula o resto
    kIndex = 0
    for key,val in indexerData.items():
        for item in val:
            result[kIndex].append(item)
            kIndex = (kIndex + 1) % k

    for x in result:
        print x

matriz = []
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])
matriz.append(["z", "y"])
matriz.append(["z", "x"])
matriz.append(["q", "y"])


kFoldCrossValidation(matriz,3)