// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/repeat-a-string-repeat-a-string
// Reprak11

function repeatStringNumTimes(str, num) {
    let palabra = ""
    for (let i=0; i < num; i++){
        palabra += str
    }
    return palabra;
}

console.log(repeatStringNumTimes(prompt("Palabra"), parseInt(prompt("No. de veces"),10)));
