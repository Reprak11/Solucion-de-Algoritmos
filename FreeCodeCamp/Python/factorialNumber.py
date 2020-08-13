# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/factorialize-a-number
# Reprak11
def factorialize(num):
    if (num <= 1 ):
        return 1
    return num * factorialize(num-1)

if __name__ == "__main__":
    print(factorialize(int(input())))