# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/finders-keepers
# Reprak11

def findElement(arr, func):
    for i in arr:
        if func(i) == True:
            return i
    return


if __name__ == "__main__":
    print(findElement([1, 3, 5, 9], lambda num : num % 2 == 0 ))