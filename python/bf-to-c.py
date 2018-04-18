def brainfuck_to_c(code):
    '''
https://www.codewars.com/kata/58924f2ca8c628f21a0001a1
Meet BrainF***. It's an esoteric programming language which was created with the
goal of having a language with the smallest possible compiler. Data in BF is stored in
a 30000 byte array, and there are exactly eight commands you can do with it.

'+': increment the current byte
'-': decrement the current byte
'<': move the data pointer left
'>': move the data pointer right
'[': if the cell under the data pointer is 0, skip to the matching ']'
']': matches with '['
',': input a byte into the current cell
'.': output the current cell (interpreted as ASCII)

Everything that's not one of those characters is ignored by the program. Here's a program that prints "Hello, World!" and a newline:
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

Obviously, this is completely useless for normal programming, but it somehow is Turing complete,
which means that it can compute anything that can be computed.
So what's better than writing a program that will convert BF code into its C equivalent? Not much, 
but one answer is actually writing BF code (see the other folder for examples).
 
input: the BF code to transpile
output: its equivalent in C, or 'Error!' if it's invalid 
 
    '''

    code = sanitize(code)
    if code == "Error!": return code
    code = optimize(code)

    repl = {
        "+": "*p += {};\n",
        "-": "*p -= {};\n",
        ">": "p += {};\n",
        "<": "p -= {};\n",
        ".": "putchar(*p);\n",
        ",": "*p = getchar();\n",
        "[": "if (*p) do {\n",
        "]": "} while (*p);\n"
    }

    ret = ""
    indent = 0
    i = 0
    while i < len(code):
        if code[i] in "+-<>":
            count = 1
            curr = code[i]
            i += 1
            while i < len(code) and code[i] == curr:
                count += 1
                i += 1
            ret += "  " * indent + repl[curr].format(count)
        else:
            if code[i] == "]":
                indent -= 1
            ret += "  " * indent + repl[code[i]]
            if code[i] == "[":
                indent += 1
            i += 1
    return ret


#removes non-command characters and checks for mismatched brackets
def sanitize(code):
    brackets = 0
    out = []
    for c in code:
        if c not in "+-<>[].,": continue
        if c == "[":
            brackets += 1
        elif c == "]":
            brackets -= 1
        if brackets < 0: return "Error!"
        out.append(c)
    return "".join(out) if brackets == 0 else "Error!"


#removes extraneous characters
def optimize(code):

    changed = True
    while changed:
        count = 0
        i = 0
        out = ""
        while i < len(code):
            c = code[i]
            if c in "+-":
                while i < len(code) and c in "+-":
                    c = code[i]
                    if c not in "+-": break
                    count += (1 if c == "+" else -1)
                    i += 1
                if count > 0:
                    out += "+" * count
                else:
                    out += "-" * (-count)
                count = 0
            elif c in "<>":
                while i < len(code) and c in "<>":
                    c = code[i]
                    if c not in "<>": break
                    count += (1 if c == ">" else -1)
                    i += 1
                if count > 0:
                    out += ">" * count
                else:
                    out += "<" * (-count)
                count = 0
            elif code[i] in "[],.":
                out += code[i]
                i += 1
            else:
                i += 1
        out = out.replace("[]", "")

        changed = len(code) != len(out)
        code = out
    return code