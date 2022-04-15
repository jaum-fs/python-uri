primeiraCarta, segundaCarta = map(int,input().split())
terceiraCarta = 0
if primeiraCarta > segundaCarta:
    terceiraCarta = primeiraCarta
elif primeiraCarta == segundaCarta:
    terceiraCarta = primeiraCarta
else:
    terceiraCarta = segundaCarta
print(terceiraCarta)