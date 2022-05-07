import time

from numpy import *


def init_table(n):
    r = int(n)
    game_table = []
    for i in range(n):
        game_table.append(['0']*n)
    return game_table


def init_blocked(s,n1,n2):
    n = random.randint(n1, n2)
    block_position = random.randint(0, s, size=(n, 2))
    return block_position


def game_pole(game_table, block_position):
    for i in range(len(block_position)):
        game_table[block_position[i][0]][block_position[i][1]] = 'X'

    return game_table


def ifwin(game_table):
    for i in range(len(game_table)):
        for j in range(len(game_table)):
            if (game_table[i][j] == '0'):
                return True

    return False

def gamepad_sizeHARD(game_table):
    size_of_gamepad = random.randint(len(game_table))
    while size_of_gamepad == 1 or size_of_gamepad == 0:
        size_of_gamepad = random.randint(len(game_table))
    field_position = random.randint(len(game_table), size=(size_of_gamepad, 2))
    return field_position


def init_gamepadHARD(game_table, field_position):
    size_of_gamepad = size(field_position)/2
    r = int(len(game_table))
    gamepad = zeros(shape=(r, r), dtype=int)
    for i in range(int(size_of_gamepad)):
        k = field_position[i][0]
        x = field_position[i][1]
        gamepad[k][x] = 1

    return gamepad


def changer(ch, pad_size, game_table):
    n = len(game_table)
    s = int(size(pad_size)/2)
    if ch == 'w':
        for i in range(s):
            i = i - 1
            if pad_size[i][0] == 0:
                pad_size[i][0] = n-1
            else:
                pad_size[i][0] = pad_size[i][0] - 1
    if ch == 's':
        for i in range(s):
            i = i - 1
            if pad_size[i][0] == n-1:
                pad_size[i][0] = 0
            else:
                pad_size[i][0] = pad_size[i][0] + 1

    if ch == 'a':
        for i in range(s):
            i = i -1
            if pad_size[i][1] == 0:
                pad_size[i][1] = n-1
            else:
                pad_size[i][1] = pad_size[i][1] - 1

    if ch == 'd':
        for i in range(s):
            i = i - 1
            if pad_size[i][1] == n-1:
                pad_size[i][1] = 0
            else:
                pad_size[i][1] = pad_size[i][1] + 1

    return pad_size


def init_easygame():
    block_position = init_blocked(7, 2, 9)
    gamePole = game_pole(init_table(8), block_position)
    pad_size = gamepad_sizeHARD(gamePole)
    game_pad = init_gamepadHARD(gamePole, pad_size)
    game = [block_position, gamePole, pad_size, game_pad]
    return game


def init_mediumgame():
    block_position = init_blocked(11, 5, 15)
    gamePole = game_pole(init_table(12), block_position)
    pad_size = gamepad_sizeHARD(gamePole)
    game_pad = init_gamepadHARD(gamePole, pad_size)
    game = [block_position, gamePole, pad_size, game_pad]
    return game


def init_hardgame():
    block_position = init_blocked(9, 5, 15)
    gamePole = game_pole(init_table(14), block_position)
    pad_size = gamepad_sizeHARD(gamePole)
    game_pad = init_gamepadHARD(gamePole, pad_size)
    game = [block_position, gamePole, pad_size, game_pad]
    return game


def init_game_super_hard():
    block_position = init_blocked(15, 8, 24)
    gamePole = game_pole(init_table(16), block_position)
    pad_size = gamepad_sizeHARD(gamePole)
    game_pad = init_gamepadHARD(gamePole, pad_size)
    game = [block_position, gamePole, pad_size, game_pad]

    return game


def rand_gampad(position):
    if position == 0:
        n = random.randint(1, 3)
        if n == 1:
            field_position = [[5, 5], [4, 5], [6, 5]]
        if n == 2:
            field_position = [[5, 5], [5, 4], [5, 6]]

    if position == 1:
        n = random.randint(1, 5)
        if n == 1:
            field_position = [[5, 5], [5, 4], [5, 6], [4, 5], [6, 5]]
        if n == 2:
            field_position = [[4, 4], [4, 5], [4, 3], [5, 4], [6, 4]]
        if n == 3:
            field_position = [[5, 5], [6, 5], [7, 5], [5, 4], [5, 3]]
        if n == 4:
            field_position  = [[5, 5], [4, 5], [4, 4], [5, 6], [5, 7]]

    if position == 2:# tutaj dopisz kolejne bo są kopie
        n = random.randint(1, 7)
        if n == 1:
            field_position = [[2, 2], [3, 2], [4, 2], [1, 2], [1, 3], [0,2]]
        if n == 2:
            field_position = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1,2],[2,0],[2,1],[3,0]]
        if n == 3:
            field_position = [[0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2,4],[3,0],[3,1],[3,2],[3,3],[3,4],[4,4]]
        if n == 4:
            field_position = [[0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 1], [2,2],[2,3],[3,1],[3,2]]
        if n == 5:
            field_position = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [2,2],[3,0],[3,1],[3,2],[3,3],[3,4]]
        if n == 6:
            field_position = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 1], [1, 3],[2,1],[2,2],[2,3]]

    return field_position