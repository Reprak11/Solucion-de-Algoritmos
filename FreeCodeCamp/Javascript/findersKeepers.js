// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/finders-keepers
// Reprak11

function findElement(arr, func) {
    const found = arr.find(element => func(element) == true);
    return found;
}

console.log(findElement([1, 3, 5, 9], num => num % 2 === 0));