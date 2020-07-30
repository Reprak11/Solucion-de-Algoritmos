// https://www.hackerrank.com/challenges/simple-array-sum/problem
// Reprak11

function simpleArraySum(ar){
    let valor = 0;
    
    /*for (let i = 0; i < ar.length;i++){
        valor += ar[i];
    }*/

    /*for (const x in ar){
        valor += ar[x]
    }*/

    valor = ar.reduce((a , b) => a + b, 0);
    

    return valor;
}



let arCount = prompt("arCount");
let ar = prompt("ar");

arCount = parseInt(arCount,10);
ar = ar.split(' ').map(arTemp => parseInt(arTemp,10));

let resul = simpleArraySum(ar);

console.log(arCount);
console.log(ar);
console.log(resul);