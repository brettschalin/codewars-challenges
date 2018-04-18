/*
https://www.codewars.com/kata/53db96041f1a7d32dc0004d2

Checks whether or not a given Sudoku board is valid.

Sudoku is played on a 9x9 grid, and the goal is to fill it in so that
each row, column and 3x3 block each only contain the numbers 1-9 once.

input:
    board: a 2D array

returns:
    'Try again!' if it's not valid or 'Finished!' if it is

*/

function doneOrNot(board){
    //test each row
    for (let i = 0; i < board.length; i++) {
      let row = new Set(board[i]);
      if (row.size != board[i].length) return 'Try again!';
    }
    //test each column
    for (let i = 0; i < board[0].length; i++) {
      let col = new Set();
      for (let j = 0; j < board.length; j++) {
        col.add(board[j][i]);
      }
      if (col.size != board.length) return 'Try again!';
    }
  
    //test 3x3 squares
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        let square = new Set();
        for(let x = 0; x < 9; x++) {
            square.add(board[3*i+(x%3)][3*j+Math.floor(x/3)]);
        }
        if (square.size != 9) return 'Try again!';
      }
    }
  return 'Finished!';
  }