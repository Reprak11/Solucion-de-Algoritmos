def gcd(a,b):
    if a <= b:
        temp = a
    if b > a:
        temp = b
    result = 1
    for i in range(2,temp+1):
        if(a%i == 0 and b%i == 0):
            result = i
    return result

def gcdRecu(a,b):
    if(b==0):
        return a
    return gcdRecu(b,a%b)

def getMyName(a,b):
    return a in b

print(gcd(10,15))
print(gcdRecu(10,15))
print(getMyName("Rodrigo",["Paco", "Rodrigo", "Paul"]))