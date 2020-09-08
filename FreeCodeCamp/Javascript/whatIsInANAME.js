// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/wherefore-art-thou
// Reprak11

function whatIsInAName(collection, source) {
    var arr = [];
    // Only change code below this line
    const valores = Object.keys(source)
    collection.forEach(element => {
        let flag = true;
        valores.forEach(llave => {
            if (!element.hasOwnProperty(llave) || !(element[llave]===source[llave])) {
                flag=false;
                }
            })
        
        if (flag==true){
            arr.push(element)
        }
        }
        
    )
    // Only change code above this line
    return arr;
}

console.log(whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" }));
console.log(whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "cookie": 2 }))
console.log(whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }, { "bat":2 }], { "apple": 1, "bat": 2 }))