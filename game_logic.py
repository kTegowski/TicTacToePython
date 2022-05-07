import time,getpass, os
from numpy import *
import pandas as pd

def isposible(game_table, block_position, changedgamepad):
    gamepadsize = int(size(changedgamepad)/2)
    blocksize = int(size(block_position)/2)
    for i in range(gamepadsize):
        if game_table[changedgamepad[i-1][0]][changedgamepad[i-1][1]] == game_table[block_position[0][0]][block_position[0][1]]:
            print("\nCHCESZ UŻYĆ ZABLOKOWANEGO POLA")
            time.sleep(1)
            break
        if i == gamepadsize -1:
            change(game_table, changedgamepad)


def change(game_table, changedgamepad):
    for i in range(int(size(changedgamepad)/2)):
        if game_table[changedgamepad[i][0]][changedgamepad[i][1]] == '0':
            game_table[changedgamepad[i][0]][changedgamepad[i][1]] = '+'
        elif game_table[changedgamepad[i][0]][changedgamepad[i][1]] == '+':
            game_table[changedgamepad[i][0]][changedgamepad[i][1]] = '0'


def point_counter(game_table):
    point_count = 0
    scale = int(len(game_table))
    for i in range(scale):
        for j in range(scale):
            if game_table[i][j] == '+':
                point_count = point_count + 1

    return int(point_count)


def score(moves_counter, min , point_count):
    score= 0.2 * int(point_count) - 1.0 * min - 0.1 * moves_counter

    return score


def timer_counter(tic):
    min, secs = divmod(time.perf_counter() - tic, 60)

    if secs < 10:
        sec = "0" + str(int(secs))
    else:
        sec = str(int(secs))
    timer = [min, sec]
    return timer


def rank():
    name = getpass.getuser()

    return name


def load_rank(position):
    if position == 0:
        name = "RankEASY.txt"
    if position == 1:
        name = "RankMEDIUM.txt"
    if position == 2:
        name = "RankHARD.txt"
    if position == 3:
        name = "RankSUPERHARD.txt"
    lines = pd.read_csv(name, sep=",", header=0)
    return lines


def write_rank(lines, user, score, moves_count, min, sec ):
    user_rank = pd.DataFrame([round(score,1), user, moves_count, str(int(min)), str(sec),])
    user_rank = user_rank.transpose()
    user_rank.columns = ['Wynik','Nazwa','LiczbaRuchów', 'Minuty', 'Sekundy']
    lines = lines.append(user_rank )

    return lines


def sort_rank(lines):
    lines = lines.sort_values(lines.columns[0], ascending=False )
    lines = lines.drop_duplicates(subset='Nazwa',keep = 'first')
    return lines


def write_file(lines, position):
    if position == 0:
        name = "RankEASY.txt"
    if position == 1:
        name = "RankMEDIUM.txt"
    if position == 2:
        name = "RankHARD.txt"
    if position == 3:
        name = "RankSUPERHARD.txt"
    file = open(name, 'w')
    wyniki = lines['Wynik'].tolist()
    nazwy = lines['Nazwa'].tolist()
    ruchy = lines['LiczbaRuchów'].tolist()
    minuty = lines['Minuty'].tolist()
    sekundy = lines['Sekundy'].tolist()
    file.write("Wynik,Nazwa,LiczbaRuchów,Minuty,Sekundy")
    for i in range(len(wyniki)):
        if i != 10:

            string1 = str(round(wyniki[i], 1)) + "," + nazwy[i] + "," + str(ruchy[i]) + "," + str(minuty[i]) + "," + str(sekundy[i])
            file.write("\n"+string1)


