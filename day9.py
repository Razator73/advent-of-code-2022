import copy

with open('input/day9.txt') as f:
    moves = [m.split(' ') for m in f.read().strip().split('\n')]
pos_H = [0, 0]
pos_T = [0, 0]


def is_touching(pos_h, pos_t):
    overlap = abs(pos_h[0] - pos_t[0]) + abs(pos_h[1] - pos_t[1]) == 0
    orthoganal = abs(pos_h[0] - pos_t[0]) + abs(pos_h[1] - pos_t[1]) == 1
    diagonal = abs(pos_h[0] - pos_t[0]) == 1 and abs(pos_h[1] - pos_t[1]) == 1
    return overlap or orthoganal or diagonal


def move_rope(pos_h, pos_t, direc, is_knot=False):
    dir_dict = {'R': [0, 1], 'L': [0, -1], 'U': [1, 0], 'D': [-1, 0]}
    if not is_knot:
        pos_h[0], pos_h[1] = pos_h[0] + dir_dict[direc][0], pos_h[1] + dir_dict[direc][1]
    if is_touching(pos_h, pos_t):
        return pos_h, pos_t
    elif pos_h[0] == pos_t[0] or pos_h[1] == pos_t[1]:
        pos_t[0], pos_t[1] = (pos_t[0] + int((pos_h[0] - pos_t[0]) / 2), pos_t[1] + int((pos_h[1] - pos_t[1]) / 2))
        return pos_h, pos_t
    else:
        return pos_h, [pos_t[0] + (1 if pos_t[0] < pos_h[0] else -1), pos_t[1] + (1 if pos_t[1] < pos_h[1] else -1)]


def move_long_rope(knots, direc):
    knots[0], knots[1] = move_rope(knots[0], knots[1], direc)
    for k in range(2, len(knots)):
        if is_touching(knots[k - 1], knots[k]):
            continue
        knots[k - 1], knots[k] = move_rope(knots[k - 1], knots[k], direc, is_knot=True)
    return knots


def print_board(knots):
    """Used for debugging purposes"""
    board = [['.' for _ in range(26)].copy() for _ in range(21)]
    board[5][11] = 's'
    for k in range(len(knot_positions) - 1, -1, -1):
        try:
            board[knots[k][0]][knots[k][1]] = str(k) if k != 0 else 'H'
        except IndexError:
            print(knots[k])
    for row in board[::-1]:
        print(' ' + ''.join(row))


# Part 1
tail_positions = []
for move in moves:
    direction, length = move[0], int(move[1])
    i = 0
    while i < length:
        pos_H, pos_T = move_rope(pos_H[:], pos_T[:], direction)
        tail_positions.append(tuple(pos_T))
        i += 1
print(f'T traveled over {len(set(tail_positions))} positions')

# Part 2
pos_H = [5, 11]
knot_positions = [pos_H.copy() for _ in range(10)]
last_knot_locs = []
for move in moves:
    direction, length = move[0], int(move[1])
    i = 0
    while i < length:
        knot_positions = move_long_rope(copy.deepcopy(knot_positions), direction)
        i += 1
        last_knot_locs.append(tuple(knot_positions[-1]))
print(f'Last knot traveled over {len(set(last_knot_locs))} positions')
