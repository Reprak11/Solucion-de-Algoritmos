// https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
// Reprak11

function plusMinus(arr){
    let cnt=[0, 0, 0];
    for (const i in arr){
        (arr[i] > 0) ? cnt[0]++ : (arr[i] < 0) ? cnt[1]++ : cnt[2]++
    }
    for (const i in cnt){
        console.log((cnt[i]/arr.length).toFixed(6))
    }
}


const n = parseInt(prompt(),10);
const arr = prompt().split(' ').map(arrTemp => parseInt(arrTemp,10));
plusMinus(arr);