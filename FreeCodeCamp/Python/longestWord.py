# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string
# Reprak11

def findLongestWordLength(str):
    str = str.split()
    size = []
    for i in str:
        size.append(len(i))
    return max(size)

if __name__ == "__main__":
    print(findLongestWordLength(input()))