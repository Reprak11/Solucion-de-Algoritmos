// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/title-case-a-sentence
// Reprak11
function titleCase(str) {
    str = str.split(" ")
    str = str.map(x => x.charAt(0).toUpperCase()+x.slice(1).toLowerCase())
    return str.join(" ");
}

console.log(titleCase(prompt("Frase de entrada")));