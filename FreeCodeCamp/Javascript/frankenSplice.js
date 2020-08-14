// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/slice-and-splice
// Reprak11
function frankenSplice(arr1, arr2, n) {    
    return arr2.slice(0,n).concat(arr1).concat(arr2.slice(n));
}

console.log(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2));