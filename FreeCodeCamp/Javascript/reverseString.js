// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/reverse-a-string
// Reprak11 
function reverseString(str) {
    let temp = []
    str.split("").forEach(element => {
       temp.unshift(element); 
    });
    str = temp.join("")
    return str;
}

function reverseString2(str){
    let expre = /./ig;
    str = str.match(expre);
    return str.reverse().join("");
}


console.log(reverseString2(prompt()));