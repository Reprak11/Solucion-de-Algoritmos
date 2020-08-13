// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/find-the-longest-word-in-a-string
// Reprak11

function findLongestWordLength(str) {
    let regex = /\w+/g
    let palabras = str.match(regex)
    palabras = (palabras.map(function(x){
        return x.length
    }));
    return Math.max(...palabras);
}

console.log(findLongestWordLength(prompt()));