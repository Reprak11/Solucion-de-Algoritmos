// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/falsy-bouncer
// Reprak11

function bouncer(arr) {
    i = 0;
    while (i < arr.length){
        if (arr[i] == false || arr[i] == 0 || arr[i] == null || arr[i] == "" || arr[i] == undefined || arr[i] == NaN){
            arr.splice(i,1);
        }
        else{
            i++;
        }
    }
    return arr;
}

// Moncake y Taynis
function bouncer2(arr) {
    return arr.filter(el => Boolean(el) !== false);
}

console.log(bouncer2([null, NaN, 1, 2, undefined]));