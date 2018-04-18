/*
https://www.codewars.com/kata/5977b5bcfd72c6a99f0000c4
Robozzle is a puzzle game, where the goal is to program a robot
to walk through a maze and collect all of the stars.

Input args:
    board: the game board, each cell is either null or an object with {color (string), star (bool)} properties
    robot: an object with {x (int), y (int), direction (string)} properties
    program: the program the robot will follow. Instructions will be to
            move, turn, repaint the current cell, or call another subroutine

    returns: an array [board, robot] representing the final states of the board and robot
            after all stars are collected
*/

robozzle = function(board, robot, program) {
  let instructions = program[0].slice().reverse();
  const width = board[0].length,
    height = board.length;
  const move = () => {
    if (['right', 'left'].includes(robot.direction)) {
      robot.x += robot.direction == 'right' ? 1 : -1;
    } else {
      robot.y += robot.direction == 'down' ? 1 : -1;
    }
    if (
      0 > robot.x ||
      robot.x >= width ||
      0 > robot.y ||
      robot.y >= height ||
      board[robot.y][robot.x] === null
    ) {
      throw 'Robot moved out of bounds!';
    } else {
      board[robot.y][robot.x].star = false;
    }
  };
  const turn = d => {
    const direction = ['up', 'right', 'down', 'left'].indexOf(robot.direction);
    if (d) {
      robot.direction = ['up', 'right', 'down', 'left'][(direction + 1) % 4];
    } else {
      robot.direction = ['up', 'left', 'down', 'right'][(direction + 1) % 4];
    }
  };
  while (
    instructions.length > 0 &&
    board.some(row => row.some(el => el !== null && el.star))
  ) {
    let cell = board[robot.y][robot.x];
    let c = instructions.pop();

    let colorConditional = !c.if ? true : cell.color === c.if;

    if (colorConditional) {
      switch (c.action) {
        case 'forward': {
          move();
          break;
        }
        case 'turn_right': {
          turn(1);
          break;
        }
        case 'turn_left': {
          turn(0);
          break;
        }
        case 'paint_blue': {
          cell.color = 'blue';
          break;
        }
        case 'paint_green': {
          cell.color = 'green';
          break;
        }
        case 'paint_red': {
          cell.color = 'red';
          break;
        }
        //call another subprogram
        default:
          let toAdd = program[c.action].slice().reverse();
          instructions.push(...toAdd);
      }
    }
  }

  if (board.some(row => row.some(el => el !== null && el.star))) {
    throw "There's still some stars left!";
  }

  return [board, robot];
};
