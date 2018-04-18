def find_word(board, word):
    '''
https://www.codewars.com/kata/57680d0128ed87c94f000bfd

Determines whether the passed word is a valid guess for a Boggle board.
Guesses can start from any square, and be connected to any adjacent square
if it isn't already in the word. For example, in the following board:

[ ['I','L','A','W'],
  ['B','N','G','E'],
  ['I','U','A','O'],
  ['A','S','R','L'] ]

'LOAN', 'GAS', 'BIN', and 'RUN' are all valid guesses. 

inputs:
    board: a 2D array of characters
    word: the word to search for

returns:
    boolean of whether word is a valid guess for board

    '''
    return any([find_helper(board,word,x,y,[]) for x,row in enumerate(board) for y,col in enumerate(row)])

def find_helper(board, word, x, y,visited):
    if not (0 <= x < len(board)) or not (0 <= y < len(board)): return False
    if [x,y] in visited: return False
    if len(word) == 1: return word == board[y][x]
    if len(word) > len(board)**2: return False
    if word[0] == board[y][x]: return any([find_helper(board,word[1:],x+dx,y+dy,visited+[[x,y]]) for dx in [-1,0,1] for dy in [-1,0,1]]