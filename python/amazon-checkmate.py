def amazon_check_mate(king, amazon):
    '''
https://www.codewars.com/kata/5897f30d948beb78580000b2

An amazon is a theoretical chess piece which can take the moves of both a queen and a knight.
For this kata, you're playing as the black king. It's just you against the white king and amazon.
Your goal is to place every possible position for your piece into one of four categories:
1. checkmate (king under attack and cannot move)
2. check (king under attack but can move)
3. stalemate (king not under attack but cannot move)
4. safe (king not under attack and can move)

input:
    positions of the white king and amazon, in standard chess notation

returns:
    an array of four numbers, corresponding to the number of squares in each
    situation described above.
    '''

    king = get_pos(king)
    amazon = get_pos(amazon)
    can_take_amazon = abs(amazon['x'] - king['x']) > 1 or abs(
        amazon['y'] - king['y']) > 1
    checkmate, check, stalemate, safe = [], [], [], []

    sign = lambda x: x and (-1, 1)[x < 0]
    for x in range(1, 9):
        for y in range(1, 9):
            dx_a, dy_a = x - amazon['x'], y - amazon['y']
            sx_a, sy_a, dx_a, dy_a = sign(dx_a), sign(dy_a), abs(dx_a), abs(
                dy_a)
            dx_k, dy_k = x - king['x'], y - king['y']
            sx_k, sy_k, dx_k, dy_k = sign(dx_k), sign(dy_k), abs(dx_k), abs(
                dy_k)
            is_safe = False
            #can't be near the white king
            if dx_k <= 1 and dy_k <= 1:
                continue
            #can't put our king ON the amazon's tile
            if dx_a == 0 and dy_a == 0:
                continue
            #queen-like moves
            elif dx_a == dy_a:
                if dx_k == dy_k and dx_a > dx_k and sx_a == sx_k and sy_a == sy_k:
                    is_safe = True
            elif x == amazon['x'] and not (x == king['x'] and
                                           (dy_a > dy_k and sy_a == sy_k)):
                pass
            elif y == amazon['y'] and not (y == king['y'] and
                                           (dx_a > dx_k and sx_a == sx_k)):
                pass
            #knight-like moves
            elif (dx_a, dy_a) in [(1, 2), (2, 1)]:
                pass
            else:
                is_safe = True
            #it's a safe tile
            if is_safe:
                safe.append([x, y])
            else:
                check.append([x, y])

    for c in check:
        add = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: continue
                if [c[0] + i, c[1] + j
                    ] in safe or (can_take_amazon and c[0] + i == amazon['x']
                                  and c[1] + j == amazon['y']):
                    add = False
        if add: checkmate.append(c)

    check = [c for c in check if c not in checkmate]

    for s in safe:
        add = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: continue
                if [s[0] + i, s[1] + j] in safe:
                    add = False
        if add: stalemate.append(s)
    safe = [s for s in safe if s not in stalemate]

    return [len(checkmate), len(check), len(stalemate), len(safe)]


def get_pos(s):
    letters = "abcdefgh"
    return {'x': letters.index(s[0]) + 1, 'y': int(s[1])}
