# https://www.hackerrank.com/contests/prueba-python/challenges/2-ciclos-blackjack
# Reprak 11
def winner(a,b):
    if (a>21 or (a<=b and b<=21)):
        print("Gana la mesa")
    else:
        print("Gana el jugador")

jugador = []
a=0
while (a!="STOP"):
    a=input()
    if(a=="STOP"):
        break
    jugador.append(int(a))

casa = []
n = int(input())
for i in range(n):
    casa.append(int(input()))

winner(sum(jugador),sum(casa))