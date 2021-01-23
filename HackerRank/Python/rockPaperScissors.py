# https://www.hackerrank.com/contests/prueba-python/challenges/1-control-de-flujo-piedra-papel-o-tijeras
# Reprak11

def result(a,b):
    if (a==b):
        return "Empate"
    if((a=="Papel" and b=="Piedra") or (a=="Piedra" and b=="Tijeras") or (a=="Tijeras" and b=="Papel")):
        return "Gano el jugador 1"
    else:
        return "Gano el jugador 2"
a = input()
b = input()

print(result(a,b))