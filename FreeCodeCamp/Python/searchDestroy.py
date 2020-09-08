# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/seek-and-destroy
# Reprak11

def destroyer(*arr):
    x = list(filter(lambda i: i not in list(arr[1:]),arr[0]))
    return x

if __name__ == "__main__":
    print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
    print(destroyer(["tree", "hamburger", 53], "tree", 53))
    print(destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"], "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan"))
