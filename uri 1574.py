def daComandos(n):
    for i in range(n):
        contador = 0
        lista = []
        qtdComandos = int(input())
        for i in range(0, qtdComandos):
            lista.append(input())
        for i in range(0, qtdComandos):
            if (lista[i] == 'LEFT'):
                contador -= 1
            elif (lista[i] == 'RIGHT'):
                contador += 1
            else:
                lista[i] = lista[i].split()
                lista[i] = lista[i][len(lista[i]) - 1]
                lista[i] = lista[int(lista[i]) - 1]
                if (lista[i] == 'LEFT'):
                    contador -= 1
                else:
                    contador += 1
        print(contador)
    return None
qtdTeste = int(input())
daComandos(qtdTeste)