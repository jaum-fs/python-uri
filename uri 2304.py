dinheiro, qtdComandos = map(int,input().split())
dinheiroD = dinheiro
dinheiroE = dinheiro
dinheiroF = dinheiro
for i in range(qtdComandos):
    comandos = input().split()
    if comandos[0]=="C":
        if comandos[1] == "D":
            dinheiroD = dinheiroD - int(comandos[2])
        elif comandos[1] == "E":
            dinheiroE = dinheiroE - int(comandos[2])
        elif comandos[1] == "F":
            dinheiroF = dinheiroF - int(comandos[2])
    if comandos[0]=="V":
        if comandos[1] == "D":
            dinheiroD = dinheiroD + int(comandos[2])
        elif comandos[1] == "E":
            dinheiroE = dinheiroE + int(comandos[2])
        elif comandos[1] == "F":
            dinheiroF = dinheiroF + int(comandos[2])
    if comandos[0]=="A":
        if comandos[1] == "D" and comandos[2]=="E":
            dinheiroD= dinheiroD+int(comandos[3])
            dinheiroE = dinheiroE-int(comandos[3])
        elif comandos[1] == "E" and comandos[2]=="D":
            dinheiroD= dinheiroD-int(comandos[3])
            dinheiroE = dinheiroE+int(comandos[3])
        elif comandos[1] == "D" and comandos[2]=="F":
            dinheiroD= dinheiroD+int(comandos[3])
            dinheiroF = dinheiroF-int(comandos[3])
        elif comandos[1] == "F" and comandos[2]=="D":
            dinheiroD= dinheiroD-int(comandos[3])
            dinheiroF = dinheiroF+int(comandos[3])
        elif comandos[1] == "E" and comandos[2] == "F":
            dinheiroE = dinheiroE + int(comandos[3])
            dinheiroF = dinheiroF - int(comandos[3])
        elif comandos[1] == "F" and comandos[2] == "E":
            dinheiroE = dinheiroE - int(comandos[3])
            dinheiroF = dinheiroF + int(comandos[3])
print(dinheiroD, dinheiroE, dinheiroF)