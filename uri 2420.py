numTerritorios = int(input())
numSeccoes = list(map(int,input().split()))
for i in range(numTerritorios):
    if sum(numSeccoes[:i]) == sum(numSeccoes[i:]):
        print(i)