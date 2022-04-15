def organizaDevolve(letras):
    palavra1 = letras[0]
    palavra2 = letras[1]
    resultado = ""
    contador = 0

    while contador < len(palavra1) and contador < len(palavra2):
        resultado += palavra1[contador] + palavra2[contador]
        contador += 1
    if contador < len(palavra1):
        resultado += palavra1[contador:]
    elif contador < len(palavra2):
        resultado += palavra2[contador:]
    print(resultado)
    return None

qtd = int(input())
while qtd!=0:
    caracteres = input().split()
    organizaDevolve(caracteres)
    qtd -= 1
