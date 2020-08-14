// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/where-do-i-belong
// Reprak11
function getIndexToIns(arr, num) {
    arr.sort((a,b) => a-b);
    for (let i = 0; i < arr.length; i++){
        if (num <= arr[i]){
            return i
        }
    }
    return arr.length;
};

//Taynis
function getIndexToIns2(arr, num) {
   return (arr.filter(e => e < num)).length;
};

console.log(getIndexToIns2([3, 10, 5], 11));
