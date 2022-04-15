def encontraPrimo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

while True:
    try:
        num = input()
        verifica = encontraPrimo(int(num))
        if not verifica:
            print("Nada")
        else:
            contador=0
            for i in range(len(num)):
                eprimo = encontraPrimo(int(num[i]))
                if eprimo:
                    contador+=1
            if contador == len(num):
                print("Super")
            else:
                print("Primo")
    except EOFError:
        break