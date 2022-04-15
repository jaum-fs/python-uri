n, m = map(int,input().split())
matriz = []

for i in range(n):
    linha = input()
    lista_str = linha.split()
    lista_int = []
    for x in lista_str:
        lista_int.append(int(x))
    matriz.append(lista_int)

melhorLugar = None

for i in range(n):
    soma = 0
    for j in range(m):
        soma += matriz[i][j]

    if melhorLugar == None:
        melhorLugar = soma
    else:
        melhorLugar = max(melhorLugar, soma)

for j in range(m):
    soma = 0

    for i in range(n):
        soma += matriz[i][j]

    melhorLugar = max(melhorLugar, soma)

print(melhorLugar)