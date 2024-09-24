/* 
https://www.hellojavascript.info/docs/intro

Note:
All JavaScript variables must be identified with unique names.
These unique names are called identifiers.

The "equal to" operator is written like == in JavaScript.

The let and const keywords were added to JavaScript in 2015.
Variables declared with let cannot be Redeclared in the same scope
{
  let x = 2;
}
// x can NOT be used here

Var Keyword:
The var keyword was used in all JavaScript code from 1995 to 2015.
The var keyword should only be used in code written for older browsers.
Variables defined with var can be redeclared.

Adding two numbers, will return the sum, 
BUT adding a number and a string will return a string

When used on strings, the + operator is called the concatenation operator.
*/

// Websites for ls practice
// https://javascript.info/
// https://skillsforall.com/launch?id=062c7386-e936-452f-a584-65e0a3355ced&tab=curriculum&view=d6d2a511-b49f-5f3c-9ef7-cece4391c238

// -------------------
// Namaste Javascript:
// -------------------

// Everything in javascript happens inside an Execution Context
    //             Execution Context
    //  Memory also known as     |   Code also known as 
    //  (Variable Environment)   |   (Thread of Execution)
    //                           |
    //  It contains variables    |   It is a place where the 
    //  and functions as key     |   code is executed one line
    //  value pair.              |   at a time. 
    //                           
    // JavaScript is a synchronous single-threaded language
    // ----------------------------------------------------
    // --> Single threaded means JavaScript can execute once command at a time
    // --> Synchronous single-threaded that means JavaScript can execute one command 
    //     at a time in a specific order.             