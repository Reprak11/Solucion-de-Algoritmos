// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/confirm-the-ending
// Reprak11

function confirmEnding(str, target) {
    let valida = true;
    for (let i = target.length-1; i >= 0;i--){
        if (target[target.length-1-i] != str[str.length-1-i]){
            valida = false
        }
    }
    return valida;
}

console.log(confirmEnding("Bastian", "ian"));