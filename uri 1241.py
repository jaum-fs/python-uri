qtdTestes = int(input())
for i in range(qtdTestes):
    a, b = input().split()
    if a[-len(b)::] == b:
        print("encaixa")
    else:
        print("nao encaixa")