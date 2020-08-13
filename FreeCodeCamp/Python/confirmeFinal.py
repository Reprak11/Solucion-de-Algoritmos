# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending
# Reprak11
def confirmEnding(str, target):
    confirmacion = False
    if (str.endswith(target)):
        confirmacion = True
    return confirmacion

print(confirmEnding(input("Palabra: "),input("Termina con: ")))