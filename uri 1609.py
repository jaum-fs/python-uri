def removeRepetidos(lista):
    naoRepetidos = []
    for i in lista:
        if i not in naoRepetidos:
            naoRepetidos.append(i)
    print(len(naoRepetidos))
    return None

qtdTeste = int(input())
for i in range(qtdTeste):
    numCarneirinhos = int(input())
    carneirinhos = list(map(int, input().split()))
    removeRepetidos(carneirinhos)