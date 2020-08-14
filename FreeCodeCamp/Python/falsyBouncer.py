# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/falsy-bouncer
# Reprak11

def bouncer(arr):
    i = 0
    while (i < len(arr)):
        if (arr[i] == False or arr[i] == None or arr[i] == "" or arr[i] == 0):
            arr.pop(i)
        else:
            i += 1
    return arr

if __name__ == "__main__":
    print(bouncer([7, "ate", "", False, 9, None, 0, "Reprak11" ]))