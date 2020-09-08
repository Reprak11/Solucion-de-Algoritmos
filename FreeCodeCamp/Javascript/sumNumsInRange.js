// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/sum-all-numbers-in-a-range
// Reprak11
function sumAll(arr) {
    if (arr[0] < arr[1]){
        return [...Array(arr[1]-arr[0]+1).keys()].map(element => element + arr[0]).reduce((a,b) => a+b,0);
    } else {
        return [...Array(arr[0]-arr[1]+1).keys()].map(element => element + arr[1]).reverse().reduce((a,b) => a+b,0);
    }
}
//T4ynis
function sumAll2(arr){
    const inicio = arr[0];
    const final = arr[1];
    const numCount = Math.abs(inicio-final)+1;
    return ((inicio+final)*numCount/2);
}


let nums = prompt("nums");
nums = nums.substring(1, nums.length-1).split(",").map(tempNum => parseInt(tempNum));

console.log(sumAll2(nums));