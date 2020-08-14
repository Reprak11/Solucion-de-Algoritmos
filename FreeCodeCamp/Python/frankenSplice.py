# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/slice-and-splice
# Reprak11

def frakenSplice(arr1, arr2, n):
    return arr2[:n] + arr1 + arr2[n:]

if __name__ == "__main__":
    print(frakenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2))
