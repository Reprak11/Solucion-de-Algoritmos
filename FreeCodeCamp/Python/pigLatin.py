# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/pig-latin
# Reprak11

def translatePigLatin(str):
    str = list(str)
    vowels = ["a", "e", "i", "o","u"]
    consonant = []
    while (not(str[0] in vowels)):
        consonant.append(str.pop(0))
    
    return "".join(str)+"".join(consonant)+"ay"

if __name__ == "__main__":
    print(translatePigLatin("consonant"))
    print(translatePigLatin("california"))
    print(translatePigLatin("paragraphs"))
    print(translatePigLatin("eight"))
    print(translatePigLatin("schwartz"))