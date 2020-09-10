function myReplace(str, before, after) {
    str=str.split(" ")
    if ((before[0].toUpperCase() == before[0])){
    str[str.indexOf(before)] = after.charAt(0).toUpperCase() + after.slice(1)
    } else {
    str[str.indexOf(before)] = after.charAt(0).toLowerCase() + after.slice(1)
    }
    return str.join(" ");
}
console.log(myReplace("Let us go to the store", "store", "mall"))
console.log(myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped"));
console.log(myReplace("I think we should look up there", "up", "Down"));
console.log(myReplace("Let us get back to more Coding", "Coding", "algorithms"))