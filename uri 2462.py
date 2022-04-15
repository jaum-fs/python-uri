def converteHorario(hora):
    h, m = hora.split(':')
    return int(h) * 60 + int(m)


pa, cb, pb, ca = map(converteHorario, input().split())

duracaoVoo = cb + ca - (pa + pb)
duracaoVoo = duracaoVoo % (60 * 24)
duracaoVoo = duracaoVoo//2

fuso = (cb - (pa + duracaoVoo)) // 60
while fuso < -11:
    fuso += 24
while fuso > 12:
    fuso -= 24

print(duracaoVoo, fuso)