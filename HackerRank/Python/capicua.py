# https://www.hackerrank.com/contests/prueba-python/challenges/5-medio-capicua-de-un-numero
# Reprak11

###ESCRIBE TU CODIGO DESPUES DE ESTA LINEA.
def es_capicua(n):
    n = str(n)
    return n==n[::-1]

def calcular_capicua(n):
    temp = n+int(str(n)[::-1]) 
    while (not es_capicua(temp)):
        temp = temp+int(str(temp)[::-1])
    return temp

def encontrar_capicua(n):
    n = str(n)
    res = 0
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if (n[i]==n[j]):
                if es_capicua(n[i:j+1]):
                    if (len(str(res)) < len(n[i:j+1]) or ((len(str(res)) == len(n[i:j+1])) and int(res) < int(n[i:j+1]))):
                        res = n[i:j+1]
    return int(res)
###HASTA AQUI LLEGA TU CODIGO

###ESTAS LINEAS SE ENCARGAN DE PROBAR TU CODIGO CON LOS CASOS DE PRUEBA. NO LAS BORRES.
input_lines = int(input())
count = 0
s = ""
while (count < input_lines):
    s += input() + "\n"
    count += 1
exec(s)

print(calcular_capicua(57))