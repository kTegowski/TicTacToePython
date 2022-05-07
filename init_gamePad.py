import random
from numpy import *


def gamepad_size(game_table):
    size_of_gamepad = random.randint(sqrt(size(game_table)))
    while size_of_gamepad == 1 or size_of_gamepad == 0:
        size_of_gamepad = random.randint(sqrt(size(game_table)))
    field_position = random.randint(sqrt(size(game_table)), size=(size_of_gamepad, 2))

    return field_position


def init_gamepad(game_table, field_position):
    size_of_gamepad = size(field_position)/2
    r = int(sqrt(size(game_table)))
    gamepad = zeros(shape=(r, r), dtype=int)
    for i in range(int(size_of_gamepad)):
        k = field_position[i][0]
        x = field_position[i][1]
        gamepad[k][x] = 1

    return gamepad


def changer(ch, pad_size):
    s = int(size(pad_size)/2)
    if ch == 'w':
        for i in range(s):
            i = i - 1
            if pad_size[i][0] == 0:
                pad_size[i][0] = 7
            else:
                pad_size[i][0] = pad_size[i][0] - 1
    if ch == 's':
        for i in range(s):
            i = i - 1
            if pad_size[i][0] == 7:
                pad_size[i][0] = 0
            else:
                pad_size[i][0] = pad_size[i][0] + 1

    if ch == 'a':
        for i in range(s):
            i = i -1
            if pad_size[i][1] == 0:
                pad_size[i][1] = 7
            else:
                pad_size[i][1] = pad_size[i][1] - 1

    if ch == 'd':
        for i in range(s):
            i = i - 1
            if pad_size[i][1] == 7:
                pad_size[i][1] = 0
            else:
                pad_size[i][1] = pad_size[i][1] + 1

    return pad_size
