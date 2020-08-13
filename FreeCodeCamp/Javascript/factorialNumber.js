// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/factorialize-a-number
// Reprak11

function factorialize(num) {
    if (num <= 1 ){
        return 1
    }
    return num * factorialize(num-1);
}

console.log(factorialize(parseInt(prompt(),10)));