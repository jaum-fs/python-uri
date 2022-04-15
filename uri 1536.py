def calculaPontosSaldoResultado(n):
    for i in range(n):
        golsFora1 = 0
        golsFora2 = 0
        pontosMandante = 0
        pontosVisitante = 0
        saldo1 = 0
        saldo2 = 0
        m1, c, v1 = map(str, input().split())
        v2, c, m2 = map(str, input().split())
        saldo1 = (int(m1) - int(v1)) + (int(m2) - int(v2))
        saldo2 = (int(v1) - int(m1)) + (int(v2) - int(m2))
        golsFora1 += int(m2)
        golsFora2 += int(v1)
        if m1 > v1:
            pontosMandante += 3
        elif v1 > m1:
            pontosVisitante += 3
        elif m1 == v1:
            pontosMandante += 1
            pontosVisitante += 1
        if v2 > m2:
            pontosVisitante += 3
        elif m2 > v2:
            pontosMandante += 3
        elif m2 == v2:
            pontosMandante += 1
            pontosVisitante += 1
        if pontosMandante > pontosVisitante:
            print("Time 1")
        elif pontosMandante < pontosVisitante:
            print("Time 2")
        elif pontosMandante == pontosVisitante:
            if saldo1 > saldo2:
                print("Time 1")
            elif saldo1 < saldo2:
                print("Time 2")
            elif saldo1 == saldo2:
                if golsFora1 > golsFora2:
                    print("Time 1")
                elif golsFora1 < golsFora2:
                    print("Time 2")
                elif golsFora1 == golsFora2:
                    print("Penaltis")
    return None

numJogos=int(input())
calculaPontosSaldoResultado(numJogos)

