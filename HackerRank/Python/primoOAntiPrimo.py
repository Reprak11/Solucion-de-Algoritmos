# https://www.hackerrank.com/contests/prueba-python/challenges/4-medio-primo-o-anti-primo
# Reprak11
def es_primo(n):
    n= int(n)
    if(n<2):
        return False

    if (n==2 or n==3):
        return True

    for i in range(2,n):
        if((n%i)==0):
            return False
    return True

def es_antiprimo(n):
    n= int(n)
    if(n<2):
        return False
    divN=1
    for i in range(1,n):
        if((n%i)==0):
            divN += 1
    
    for i in range(1,n):
        temp=1
        for j in range(1,i):
            if((i%j)==0):
                temp += 1
        if(temp > divN):
            return False
    print(divN)
    return True

def divisores_comun(a,b):
    a= int(a)
    b= int(b)
    x= a if a<=b else b
    for i in range(1,x):
        if ((a%i)==0) and ((b%i)==0):
            print(i)

input_lines = int(input())
count = 0
s = ""
while (count < input_lines):
    s += input() + "\n"
    count += 1

exec(s)
print(es_antiprimo(10080))