// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/seek-and-destroy
// Reprak11

function destroyer(...arr) {
    const valores = arr[0]
    const filtro = arr.slice(1)
    return valores.filter(element => !filtro.includes(element))
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3));