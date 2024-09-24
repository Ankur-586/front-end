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

// ----------------------------------- Notes -------------------------------------

// -------------------
// Namaste Javascript: https://youtube.com/playlist?list=PLlasXeu85E9cQ32gLCvAvr9vNaUccPVNP&si=urzGlz8T4qeO09y8
// -------------------
// Execution context: the environment in which JavaScript code is executed.

// Video 1:
// Everything in javascript happens inside an Execution Context
// ---------------------------------------------------------------
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

// Video 2:
/* 
-> What happens when you run a js program?
   function square(num) { num is parameter
    var ans = num * num; 
    return ans;
    }
    var n = 2;
    var square2 = square(n); n is argument
    var square4 = square(4); 
    console.log(square2,square4)
    // to run js in terminal : node js_notes.js

    **** js skims through the whole pgm line by line.

    | My own Written Explaination
    |------------------------------------------------------------------------------------------------------
    |Phase 1: Memory creation phase:
    |------- 
    |step 1: An execution context is created and it is the Global Execution Context.
    |step 2: space for variale and functions are assinged in memory part
    |        n: undefined  (when it allocates memeory to a variable it provides a special value undefined)
    |        square: {...} (And for function it litreally stores whole code of the function)
    |        square2 : undefined
    |        square4 : undefined
    |
    |Phase 2: Code exectuion phase: In this all the calculation in the program is done.
    |--------
    |    step 1: In this phase the value 2 is being place in the place holder n.
    |    Phase 1:
    |    --------
    |    step 1: when var square2 = square(n); this line runs and function is invoked,
    |            a new Execution Context is created for the instance square2.
    |    step 2: now in the Memory creation phase:
    |            the function's variables get value undefined:
    |            num: undefined , ans: undefined
    |    Phase 2: 
    |    --------
    |    step 1: Now, in the num varaiable 2 will be assigned to it 
    |                 and in ans the output of num * num
    |    Whenever return keyword is encountered , it means the task of function is over and it returns back the control 
    |    of the program back to the place where it was invoked.
    |
    |    ****IMP*** And after that the value which is returned will get stored in:
    |            square2 : 4 (earlier undefined was stored)
    |    Now, when the var square2 = square(n); instance of the function (here, square2) done executing  
    |         then the whole Execution Context (which was created for the instance of function) gets deleted.
    |    And when var square4 = square(4); this is encountered then the same process will be done.
    --------------------------------------------------------------------------------------------------------------------

    Below is the more clear systematic by chatgpt:
    1. Memory Creation Phase
    When a JavaScript program runs, the first step is the Memory Creation Phase. Here’s what happens:
    > Global Execution Context is created, which is the environment where the code runs.
    > Space is allocated for variables and functions:
      . n is declared, so it starts as undefined.
      . square holds a reference to the function's code.
      . square2 and square4 are also initialized as undefined.

    2. Code Execution Phase
    In this phase, the actual execution of the code occurs:
    > Assigning Values:
      . When var n = 2; runs, n is assigned the value 2.
    > Function Invocation:
      > For var square2 = square(n);, the function square is called:
        . A new Execution Context for square is created.
        > Memory is allocated for the parameters and local variables:
          . num is assigned undefined initially.
          . After assigning num the value of n (which is 2), it calculates ans = num * num, resulting in 4.
        > The function returns 4, which is stored in square2.
    > After this execution context completes, it is cleaned up, and memory is freed.
    > The same steps occur for var square4 = square(4);, where num takes the value 4, leading to a return value of 16 stored in square4.
*/

