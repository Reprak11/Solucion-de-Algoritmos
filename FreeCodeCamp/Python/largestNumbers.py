# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/return-largest-numbers-in-arrays
# Reprak11

def largestOfFour(arr):
    numMAX = []
    for i in arr:
        numMAX.append(max(i))
    return numMAX

if __name__ == "__main__":
    print(largestOfFour([[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]))