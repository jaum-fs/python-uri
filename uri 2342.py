maiorNumero = int(input())
conta = input().split()
conta[0] = int(conta[0])
conta[2] = int(conta[2])
resultado = 0
if conta[1] == "+":
    resultado = conta[0]+conta[2]
elif conta[1] == "*":
    resultado = conta[0]*conta[2]
if resultado > maiorNumero:
    print("OVERFLOW")
else:
    print("OK")