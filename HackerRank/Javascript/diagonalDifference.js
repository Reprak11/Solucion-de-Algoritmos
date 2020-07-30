// https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
// Reprak11

function diagonalDifference(arr){
    let valor1 = 0;
    let valor2 = 0;
    for (let i in arr){
        valor1 += arr[i][i];
        valor2 += arr[i][arr.length-1-i]
    }
    return Math.abs(valor2-valor1);
}


let n = prompt("n");
n = parseInt(n,10);

let arr = Array(n);


for (let i = 0; i < n; i++){
    arr[i]=prompt("arr");
    arr[i] = arr[i].split(' ').map(arrTemp => parseInt(arrTemp,10));
}
console.log(diagonalDifference(arr));