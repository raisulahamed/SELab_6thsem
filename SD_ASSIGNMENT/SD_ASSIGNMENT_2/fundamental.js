//Working with Variables and Data Types and type convsersion
let strNum = "42";
let floatNum = "42.5";

let intVal = parseInt(strNum);
let floatVal = parseFloat(floatNum);
let numVal = Number(strNum);
let strVal = String(100);
console.log(intVal, floatVal, numVal, strVal);

let a = 10, b = 5, x = true, y = false;
console.log(a + b, a - b, a * b, a / b, a % b);
console.log(x && y, x || y, !x);
console.log(a > b, a < b, a == "10", a === "10", a !== b);


//FUNCTION 
function sum1(a, b) {
    return a + b;
}

console.log(sum1(5, 3)); // Output: 8



//arrow function
const sum2 = (a, b) => a + b;

console.log(sum2(5, 3)); // Output: 8

//if-else statement:
let num = 4;

if (num % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}


//loop
for (let i = 1; i <= 10; i++) {
    console.log(i);
}



//Class and Constructor
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}
let person1 = new Person("Amjad", 23);
person1.greet(); 