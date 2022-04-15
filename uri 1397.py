qtdPartidas = int(input())
pontosJ1 = 0
pontosJ2 = 0
while qtdPartidas != 0:
    num1, num2 = map(int,input().split())
    if num1 > num2:
        pontosJ1+=1
    elif num2>num1:
        pontosJ2+=1
    qtdPartidas-=1
    if qtdPartidas == 0:
        print(pontosJ1,pontosJ2)
        pontosJ1 = 0
        pontosJ2 = 0
        qtdPartidas = int(input())