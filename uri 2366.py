postosAgua, distanciaMaxima = map(int, input().split())
distancia = list(map(int, input().split()))
distancia.append(42195)
x = 0
for i in range(1, postosAgua + 1):
    if distancia[i] - distancia[i - 1] > distanciaMaxima:
        x = 1
if x == 1:
    print("N")
else:
    print("S")