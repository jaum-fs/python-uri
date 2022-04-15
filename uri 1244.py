def ordenaLista(palavras):
    palavras.sort(key=len, reverse=True)
    for i in range(len(palavras)):
        print(palavras[i], end='')
        if i != len(palavras)-1:
            print(' ', end='')
    print()
    return None

qtdTeste = int(input())
while qtdTeste!= 0:
    strings = input().split()
    ordenaLista(strings)
    qtdTeste -=1