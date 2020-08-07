// https://leetcode.com/problems/running-sum-of-1d-array/
// Reprak11

var runningSum2 = function(nums) {
    let accum=0;
    let result = [];
    nums.forEach((element) => {
        accum += element;
        result.push(accum);
    });
    return result
};
var runningSum = function(nums) {
    let accum=0;
    let result = [];
    nums.map(function(x){
        accum += x;
        result.push(accum);
    })
    return result
};

let nums = prompt("nums")
nums = nums.substring(1,nums.length-1).split(",").map(tempNums => parseInt(tempNums,10));
console.log(runningSum2(nums));