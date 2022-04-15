numParticipantes = int(input())
x = 1
while numParticipantes > 0 and numParticipantes <= 10000:
    numIngressos = list(map(int,input().split()))
    for i in numIngressos:
        if i-1 == numIngressos.index(i):
            print("Teste",x)
            print(i)
            print()
            x+=1
    numParticipantes = int(input())