// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/mutations
// Reprak11

//Buffer
function mutation(arr) {
    let encontrado = true;
    for (let i of arr[1].toLowerCase()){
        let re = new RegExp("["+i+"]")
        if (re.test(arr[0].toLowerCase()) == false){
            encontrado = false
        }
    }
    return encontrado;
}

//justadhoc 
function mutation2(arr){
    let encontrado = true
    const set1 = new Set(arr[0].toLowerCase())
    const palabra = arr[1].toLowerCase().split("")
    palabra.forEach(element => {
        if(set1.has(element) == false){
            encontrado = false
        }
    });
    return encontrado
}
function mutation3(arr){
    const s = new Set(arr[0].toLowerCase()) 
    return !arr[1].split('').find(c => !s.has(c.toLowerCase()))
}
console.log(mutation3(["hello", "neo"]));