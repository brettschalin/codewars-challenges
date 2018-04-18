/*
https://www.codewars.com/kata/526a569ca578d7e6e300034e

Converts between two different bases.

The kata defines a few alphabets already, such as BINARY ('01') or HEXA_DECIMAL ('0123456789abcdef'),
and this program will convert numbers between those bases.
Examples:
    convert('15', alphabet.DECIMAL, alphabet.BINARY) == '1111'
    convert("1011", Alphabet.BINARY, Alphabet.HEXA_DECIMAL); // should return "b"

inputs:
    input: the number to convert (as a string)
    source: base to convert from (this is the base of the input)
    target: base to convert to

returns:
    the input number converted to the target base

*/

function convert(input, source, target) {

    let num = 0;
    for ( let i = input.length-1; i >= 0; i-- ) {
      num += source.indexOf(input[i]) * Math.pow(source.length, input.length - i - 1);
    }
  
    let output = [];
    while (num > 0) {
      output.unshift(target[num % target.length]);
      num = Math.floor( num / target.length );
    }
  
    return output.length?output.join(""):target[0];
  }