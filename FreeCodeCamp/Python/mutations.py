# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/mutations
# Reprak11

def mutation(arr):
    encontrado = True
    for i in arr[1].lower():
        if i not in arr[0].lower():
            encontrado = False
    return encontrado

if __name__ == "__main__":
    print(mutation(["Noel", "Ole"]))