linhas = []
for i in range(4):
    linhas.append(str(input()))
colunas = []
for i in range(len(linhas[0])):
    f = int(linhas[0][i]) * 1000
    f += int(linhas[1][i]) * 100
    f += int(linhas[2][i]) * 10
    f += int(linhas[3][i])
    colunas.append(f)
for i in range(1, len(colunas)-1):
    print(chr((colunas[0] * colunas[i] + colunas[-1]) % 257), end='')
print()