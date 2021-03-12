def checkPrime(num):
    if num < 2:
        return "Is not a prime number"
    for i in range(2,num):
        if(num%i == 0):
            return "Is not a prime number"
    return "Is a prime number"


for i in range(51):
    print(i, checkPrime(i))