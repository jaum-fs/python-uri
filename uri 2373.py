numBandejas = int(input())
coposQuebrados = 0
for i in range(numBandejas):
    numLatas, numCopos = map(int,input().split())
    if numLatas > numCopos:
        coposQuebrados += numCopos
print(coposQuebrados)