// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/truncate-a-string
// Reprak11
function truncateString(str, num) {
    let palabra = ""
    if (num > str.length){
        num = str.length
    }
    for (let i =0; i < num; i++){
        palabra += str[i];
    }
    if (palabra.length < str.length){
        palabra += "..."
    }
    
    return palabra;
}

console.log(truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length + 2));