numTeste= int(input())
for i in range(numTeste):
    qtdAlunos = int(input())
    lista1 = list(map(int, input().split()))
    lista2 = sorted(lista1)
    lista2.reverse()
    nao_mudou = qtdAlunos
    for i in range(qtdAlunos):
        if lista2[i] != lista1[i]:
            nao_mudou-=1
    print(nao_mudou)
