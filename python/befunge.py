from random import choice
def interpret(code):
    '''
https://www.codewars.com/kata/526c7b931666d07889000a3c
An interpreter for the esoteric language Befunge-93.
Befunge is different from most languages in that its code (a) is stored in a 2d array
and (b) can be modified while the program is running.

Data is stored in a stack, and can be manipulated by various commands.
The code pointer starts in the top right corner moving right, but can be reflected
to move in any direction, making the behavior of the code difficult to track.

As an example of how confusing this can get, the following code will print '123456789':

>987v>.v
v456<  :
>321 ^ _@
    '''
    def move(pointer, direction):
        new_x = (pointer[1] + direction[1])%max_x
        new_y = (pointer[0] + direction[0])%max_y
        return (new_y, new_x)
    output = ""
    pointer = (0,0)
    direction = (0,1)
    stack = []
    code = [[x for x in row] for row in code.splitlines()]
    max_x, max_y = max([len(row) for row in code]), len(code)
    string_mode = False
    while True:
        code_point = code[pointer[0]][pointer[1]]
        if string_mode:
            if code_point == '"':
                string_mode = False
            else:
                stack.append(ord(code_point))
            pointer = move(pointer, direction)
            continue
        if code_point in '0123456789':
            stack.append(int(code_point))
        elif code_point == '+':
            stack.append(stack.pop() + stack.pop())
        elif code_point == '-':
            stack.append(-stack.pop() + stack.pop())
        elif code_point == '*':
            stack.append(stack.pop()*stack.pop())
        elif code_point == '/':
            a,b = stack.pop(), stack.pop()
            stack.append(0 if a == 0 else b//a)
        elif code_point == '%':
            a,b = stack.pop(), stack.pop()
            stack.append(0 if a == 0 else b%a)
        elif code_point == '!':
            stack.append(0 if stack.pop() else 1)
        elif code_point == '`':
            a,b = stack.pop(), stack.pop()
            stack.append(1 if b>a else 0)
        elif code_point == '>':
            direction = (0,1)
        elif code_point == '<':
            direction = (0,-1)
        elif code_point == '^':
            direction = (-1,0)
        elif code_point == 'v':
            direction = (1,0)
        elif code_point == '?':
            direction = choice([(0,1),(0,-1),(1,0),(-1,0)])
        elif code_point == '_':
            direction = (0, 1 - 2*(stack.pop()!=0))
        elif code_point == '|':
            direction = (1 - 2*(stack.pop()!=0), 0)
        elif code_point == '"':
            string_mode = True
        elif code_point == ':':
            if len(stack):
                stack.append(stack[-1])
            else:
                stack.append(0)
        elif code_point == '\\':
            if len(stack)>1:
                stack[-2:] = stack[-2:][::-1]
            else:
                stack.append(0)
        elif code_point == '$':
            stack.pop()
        elif code_point == '.':
            output += str(stack.pop())
        elif code_point == ',':
            output += chr(stack.pop())
        elif code_point == '#':
            pointer = move(pointer, direction)
        elif code_point == 'p':
            y,x,v = stack.pop(), stack.pop(), stack.pop()
            if 0<=x<max_x and 0<=y<max_y:
                code[y][x] = chr(v)
        elif code_point == 'g':
            y,x = stack.pop(), stack.pop()
            if 0<=x<max_x and 0<=y<max_y:
                stack.append(ord(code[y][x]))
            else:
                stack.append(0)
        elif code_point == '@':
            break
        pointer = move(direction, pointer)
    return output