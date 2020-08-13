# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/reverse-a-string
# Reprak11

def reverseString(str):
    temp = ""
    for i in reversed(range(len(str))):
        temp += str[i]
    str = temp
    return str;

if __name__ == "__main__":
    print(reverseString(input()))