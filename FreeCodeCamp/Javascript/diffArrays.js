// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/diff-two-arrays
// Reprak11
function diffArray(arr1, arr2) {
    let newArr = arr2.filter(element => !arr1.includes(element)).concat(arr1.filter(element => !arr2.includes(element)));
    return newArr;
}

console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]));
console.log(diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]))
