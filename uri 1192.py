def transformaCaracterEmNumero(caract):
    lista = []
    for i in range(3):
        if i == 0 or i == 2:
            lista.append(int(caract[i]))
        else:
            lista.append(caract[i])
    return lista

def calculaResultado(lista):
    if lista[1].isupper() == True and lista[0] != lista[2]:
        print(lista[2]-lista[0])
    elif lista[1].isupper() == False and lista[0] != lista[2]:
        print(lista[0]+lista[2])
    else:
        print(lista[0]*lista[2])
    return None

casoDeTeste = int(input())
while casoDeTeste != 0:
    caracteres = input()
    calculaResultado(transformaCaracterEmNumero(caracteres))
    casoDeTeste -= 1
