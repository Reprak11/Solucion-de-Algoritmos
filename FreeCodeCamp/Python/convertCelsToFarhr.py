# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/convert-celsius-to-fahrenheit
# Reprak11

def convertToF(celsius):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit


if __name__ == "__main__":
    print(convertToF(-10))