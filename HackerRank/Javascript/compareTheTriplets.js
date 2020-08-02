// https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen
// Reprak11
"use strict";

function compareTriplets (a ,b){
    const puntos = [0,0];
    for (const i in a){
        a[i] > b[i] ? puntos[0]++ : a[i] < b[i] ? puntos[1]++ : "";
    }
    return puntos
};



let a = prompt("a");
let b = prompt("b");

a= a.split(' ').map(aTemp => parseInt(aTemp,10));
b= b.split(' ').map(bTemp => parseInt(bTemp,10));

let resul = compareTriplets(a,b);

console.log(a);
console.log(b);
console.log(resul);



/** georgedelaselva12 solution **/

function compareTriplets(a, b) {

    const awards=[0,0]

    a.forEach((val,index)=>{
        if(b[index]==a[index]) return false
       return val>b[index] ? awards[0]++ : awards[1]++;
    })

    return awards
}
