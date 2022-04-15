def verificaSequencia(lin, sub):
    existeEmSubsequencia = 0
    index = 0
    for i in lin:
        if i == sub[index]:
            existeEmSubsequencia += 1
            index += 1
            if existeEmSubsequencia == len(sub):
                return True
    return False

for j in range(int(input())):
    linha = input()
    for i in range(int(input())):
        subsequencia = input()
        if verificaSequencia(linha, subsequencia):
            print('Yes')
        else:
            print('No')