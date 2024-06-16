/* 
Note:
The var keyword was used in all JavaScript code from 1995 to 2015.
The let and const keywords were added to JavaScript in 2015.

Var Keyword:
The var keyword should only be used in code written for older browsers.
Variables declared with let cannot be Redeclared in the same scope


*/


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
    return word === word.split('')
}

word = Nun
let palin_word = palin_drome(word)
console.log(palin_word)