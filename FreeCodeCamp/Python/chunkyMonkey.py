# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/chunky-monkey
# Reprak11
import math

def chunkArrayInGroups(arr, size):
    arreglo = []
    contadora = 0
    for i in range(0,math.floor(len(arr)/size)):
        arreglo.append(arr[contadora:contadora+size])
        contadora += size
    if (len(arr)%2 != 0):
        arreglo.append(arr[contadora:])
    return arreglo

if __name__ == "__main__":
    print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3))