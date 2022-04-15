def contaVezes(x, y):
    for i in range(len(x)):
        if x[i] == y[i]:
            return False
    return True

sequencia = str(input())
palavra = str(input())
q = len(sequencia) - len(palavra) + 1
t = len(palavra)
quantidadeVezes = 0
for i in range(q):
    if contaVezes(sequencia[i:t+i], palavra):
        quantidadeVezes+= 1
print(quantidadeVezes)