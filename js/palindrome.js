/*
https://www.codewars.com/kata/59f0ee47a5e12962cb0000bf

This was a fun challenge that I made into a one-liner. The function expects an
input of two numbers, and will return the palindrome that corresponds to them.

inputs:
    a: how many digits the number has
    b: if the a-digit palindromes were arranged in increasing order, b is its index in that seqence
    
    examples:
        palin(4,2) == 1111
        palin(5,1) == 10001
        palin(5, 15) == 11411
*/

function palin(a,b){
    return (a==1?b:(a==2?b*11:(function (x) {return parseInt(x.concat(x.split("").reverse().join("").substr(a%2)))})((Math.pow(10,Math.floor((a-1)/2)) - 1 + b).toString())));
  }