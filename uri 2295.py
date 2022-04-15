precoAlcool, precoGasolina, rendimentoAlcool, rendimentoGasolina = map(float,input().split())
precoKmAlcool = 1*precoAlcool/rendimentoAlcool
precoKmGasolina = 1*precoGasolina/rendimentoGasolina
if precoKmAlcool<precoKmGasolina :
    print("A")
elif precoKmAlcool == precoKmGasolina :
    print("G")
else:
    print("G")