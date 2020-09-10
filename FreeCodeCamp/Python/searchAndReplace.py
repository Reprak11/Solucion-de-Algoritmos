# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/search-and-replace
# Reprak11
def myReplace(str, before, after):
    if before[0].isupper():
        after=after.capitalize()
        print(after)
    else:
        after=after.lower()
    str = str.split(" ")
    str[str.index(before)] = after
    return str

if __name__ == "__main__":
    print(myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped"))
    print(myReplace("He is Sleeping on the couch", "Sleeping", "sitting"))
    print(myReplace("I think we should look up there", "up", "Down"))