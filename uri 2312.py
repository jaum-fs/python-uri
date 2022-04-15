from functools import cmp_to_key
def ordena(pais1,pais2):

    return None

qtdPaises = int(input())
paisesMedalhas = []
for i in range(qtdPaises):
    infos = input().split()
    infos[1] = int(infos[1])
    infos[2] = int(infos[2])
    infos[3] = int(infos[3])
    paisesMedalhas.append(infos)
print(paisesMedalhas)
paisesMedalhas.sort(key = cmp_to_key(ordena))
for i in range(qtdPaises):
    print(paisesMedalhas[i])
