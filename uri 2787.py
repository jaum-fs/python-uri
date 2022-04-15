numLinhas = int(input())
numColunas = int(input())

if numLinhas % 2 == 0:
    if numColunas % 2 == 0:
        print("1")
    else:
        print("0")
if numLinhas % 2 != 0:
    if numColunas % 2 != 0:
        print("1")
    else:
        print("0")
