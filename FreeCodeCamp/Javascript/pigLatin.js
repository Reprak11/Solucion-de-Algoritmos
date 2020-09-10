// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/search-and-replace
// Reprak11

function translatePigLatin(str) {
    const vowels = ["a","e","i","o","u"];
    const consonant = str.split(/([aeiou].*)/gi);
    console.log(consonant);
    if (consonant[0] == ""){
        return consonant[1]+"way"
    } else if (consonant.length == 1){
        return consonant+"ay";
    }
    return consonant[1]+consonant[0]+"ay";
}

console.log(translatePigLatin("consonant"));
console.log(translatePigLatin("california"));
console.log(translatePigLatin("eight"));
console.log(translatePigLatin("schwartz"));
console.log(translatePigLatin("rhythm"))