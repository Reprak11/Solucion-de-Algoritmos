// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/chunky-monkey
// Reprak11

function chunkArrayInGroups(arr, size) {
    let arreglo = []
    let contador = 0
    for (let i = 0 ; i < Math.floor(arr.length/size);i++){
        arreglo.push(arr.slice(contador,contador+size))
        contador += size;
    }
    if (arr.length%size != 0){
        arreglo.push(arr.slice(contador))
    }
    return arreglo;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d","e"], 2));