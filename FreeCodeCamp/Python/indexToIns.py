# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/where-do-i-belong
# Reprak11
def getIndexToIns(arr,num):
    arr.sort()
    for i in range(len(arr)):
        if(num <= arr[i]):
            return i
    return len(arr)

if __name__ == "__main__":
    print(getIndexToIns([3, 10, 5], 11))