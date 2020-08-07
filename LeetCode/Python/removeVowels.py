# https://leetcode.com/problems/remove-vowels-from-a-string/
# Reprak11

def removeVowel(palabra):
    vocales = ('a','e','i','o','u')
    palabra = palabra.lower()
    for x in palabra:
        if x in vocales:
            palabra=palabra.replace(x,"")
    print(palabra)
        


if __name__ == "__main__":
    palabra = input()
    (removeVowel(palabra));