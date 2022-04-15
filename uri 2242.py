risada = input()
vogais = ""
for i in risada:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vogais+=i
if(vogais == vogais[::-1]):
    print("S")
else:
    print("N")