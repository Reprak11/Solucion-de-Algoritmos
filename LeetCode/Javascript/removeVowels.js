// https://leetcode.com/problems/remove-vowels-from-a-string/
// Reprak11

let removeVowels = function(palabra){
    const vocales = ['a','e','i','o','u'];
    palabra = palabra.toLowerCase();
    for (const x of palabra){
        if (vocales.includes(x)){
            palabra = palabra.replace(x,"");
        }
    }
    console.log(palabra);
};

//bufferoverflow12
let removeVowels2 = function(palabra){
    palabra = palabra.toLowerCase();
    const vocales = /[^aeiou]/g;
    palabra = palabra.match(vocales).join("");
    console.log(palabra);
};
//bufferoverflow12
let removeVowels3 = function(palabra){
    palabra = palabra.toLowerCase();
    const vocales = /[^aeiou]/g;
    palabra = palabra.replace(vocales,"")
    console.log(palabra);
};

let palabra = prompt();
removeVowels2(palabra);