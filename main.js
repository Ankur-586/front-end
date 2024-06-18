"use strict";

let firstName = "John",
lastName = "Doe",
age = 35;

// alert(10 + 5);
// alert(10 / 2);
// alert(15 % 9);

// 1. Write a JavaScript function to calculate the sum of two numbers. 
function test(a,b) {
    return a + b
}
let res = test(2,2)
console.log(res)

// 2. Write a JavaScript program to find the maximum number in an array. 
// console.log(arr.sort(function(arr){return arr[-1]}))
// arr[arr.lenght - 1]

function max_return(arr) {
    return Math.max(...arr)
}

const a = [3,4,2,1]
let max_res = max_return(a)
console.log(max_res)

// 3. Write a JavaScript function to check if a given string is a palindrome (reads the same forwards and backwards). 
// Nun, Madam, Racecar

function palin_drome(word) {
    return word === word.split('').reverse().join('')
}

let word = 'NuN'
let palin_word = palin_drome(word)
console.log(palin_word)

// Write a JavaScript program to reverse a given string.

const rev_str = (str) => str.split('').reverse().join('') 

let str = 'pankaj'
let str_rev = rev_str(str)
console.log(str_rev) 

// Write a JavaScript function that takes an array of numbers and returns a new array with only the even numbers. 

function even_nums(array) {
    return array.filter(num => num % 2 === 0) 
}

const arr = [1,2,3,5,6]
let even = even_nums(arr)
console.log(even)

let _ = 'z'
console.log(_)

let message;

message = 'Hello!';

message = 'World!'; // value changed
console.log(message); // returns 'World!'

// 'use strict';
// let messages = 'This';
// // repeated 'let' leads to an error
// let messages = 'That'; // SyntaxError: 'message' has already been declared

"use strict";
let myVariable = "Hello, JavaScript!";
console.log(myVariable); // error thrown

// Write a JavaScript program to calculate the factorial of a given number. 
function fact_num (num){
    if (num === 0 || num === 1)  {
        return 1
    }
    else {
        return num * fact_num(num - 1) 
    }
}

let number = 5
let x = fact_num(number)
console.log(x)

// Write a JavaScript function to check if a given number is prime. 

function check_prime (num) {
    
}
let prime_number = 4
let num = check_prime(prime_number)
console.log(num)

// Write a JavaScript program to find the largest element in a nested array.

function convert(arr) {
    let s = '';
    for (let i of arr) {
        for (let j of i) {
            s = s + String(j);
        }
    }
    let x = Array.from(s);
    let maxChar = Math.max(...x);  // Finding maximum ASCII value (not the character itself)
    console.log(String.fromCharCode(maxChar), x);
}

let array = [[1, 3], [4, 2]];
convert(array);

// Write a JavaScript function that returns the Fibonacci sequence up to a given number of terms.
