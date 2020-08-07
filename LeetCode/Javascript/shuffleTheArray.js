var shuffle = function(nums, n) {
    let resul = []
    for (let i=0; i<n; i++){
        resul.push(nums[i]);
        resul.push(nums[i+n]);
    }
    return resul;
};

let nums = prompt("nums")
nums = nums.substring(1,nums.length-1).split(",").map(tempVar => parseInt(tempVar,10));
let n = parseInt(prompt("n"),10);

console.log(shuffle(nums,n));