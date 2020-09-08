# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/spinal-tap-case
# Reprak11

def spinalCase(str):
    str = str.lower().split(" ")
    return "-".join(str)

if __name__ == "__main__":
    print(spinalCase('This Is Spinal Tap'));