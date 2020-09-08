# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/diff-two-arrays
# #Reprak11
def diffArray(arr1, arr2):
    
    print(set(arr1))
    print(set(arr2))
    newArr = list(set(arr1)-set(arr2))+list(set(arr2)-set(arr1))
    return newArr;

if __name__ == "__main__":
    print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))
    print(diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]))