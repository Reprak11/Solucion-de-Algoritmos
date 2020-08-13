# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/repeat-a-string-repeat-a-string
# Reprak11

def repeatStringNumTimes(str, num):
    result=""
    for i in range(num):
        result += str
    return result


if __name__ == "__main__":
    print(repeatStringNumTimes(input("Palabra: "), int(input("No. de Veces: "))))