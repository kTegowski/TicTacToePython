import Log_file
import init_game
import init_gamePad
import printer
import game_logic
from modules.get_char import *
import time


# Wczytywanie gry - logo

Log_file.print_log()
Log_file.print_rules()

#Wybór poziomu trudności

position = 0
printer.print_menu(position)
while True:
    ch = get_nonblock_char(0.5)
    position = printer.choice_menu(ch, position)
    if ch == 'd' or ch == 'a':
        printer.print_menu(position)
    if ch == '\n':
        break

#inicjalizacja gry

moves_counter = 0
point_count = 0
if position == 0: #Poziom łatwy
    block_position = init_game.init_blocked(7, 5, 15)
    game_table = init_game.game_pole(init_game.init_table(8), block_position)
    pad_size = init_game.rand_gampad(position)
    game_pad = init_game.init_gamepadHARD(game_table, pad_size)

if position == 1: # Poziom średni
    block_position = init_game.init_blocked(11, 15, 25)
    game_table = init_game.game_pole(init_game.init_table(12), block_position)
    pad_size = init_game.rand_gampad(position)
    game_pad = init_game.init_gamepadHARD(game_table, pad_size)

if position == 2: # Poziom trudny
    block_position = init_game.init_blocked(13, 20, 30)
    game_table = init_game.game_pole(init_game.init_table(14), block_position)
    pad_size = init_game.rand_gampad(position)
    game_pad = init_game.init_gamepadHARD(game_table, pad_size)

if position == 3: # Poziom super-trudny
    block_position = init_game.init_blocked(15, 25, 40)
    game_table = init_game.game_pole(init_game.init_table(16), block_position)
    pad_size = init_game.gamepad_sizeHARD(game_table)
    game_pad = init_game.init_gamepadHARD(game_table, pad_size)


tic = time.perf_counter()
printer.printer(game_table, pad_size, block_position)

#głowna pętla programu

while init_game.ifwin(game_table):
    ch = get_nonblock_char(0.5)
    printer.print_gameStatus(game_logic.timer_counter(tic)[0],game_logic.timer_counter(tic)[1], moves_counter, point_count)
    if ch != '':
        changedGamepad = init_game.changer(ch, pad_size, game_table)
        printer.printer(game_table,changedGamepad , block_position)
        printer.print_gameStatus(game_logic.timer_counter(tic)[0],game_logic.timer_counter(tic)[1], moves_counter, point_count)
        if ch == '\n':
            game_logic.isposible(game_table, block_position, changedGamepad)
            moves_counter += 1
            point_count = game_logic.point_counter(game_table)
            printer.printer(game_table, changedGamepad, block_position)
            printer.print_gameStatus(game_logic.timer_counter(tic)[0],game_logic.timer_counter(tic)[1], moves_counter, point_count)
        if ch == 'r':
            lines = game_logic.sort_rank(game_logic.write_rank(game_logic.load_rank(position), game_logic.rank(), game_logic.score(moves_counter, game_logic.timer_counter(tic)[0], point_count), moves_counter,game_logic.timer_counter(tic)[0],game_logic.timer_counter(tic)[1]))
            game_logic.write_file(lines, position)
            printer.print_rank(lines)
            input("Wciśnij enter aby zakończyć program: ")
            sys.exit()


#Napis końcowy


Log_file.print_win()
lines = game_logic.sort_rank(game_logic.write_rank(game_logic.load_rank(position), game_logic.rank(), game_logic.score(moves_counter, game_logic.timer_counter(tic)[0], point_count), moves_counter,game_logic.timer_counter(tic)[0],game_logic.timer_counter(tic)[1]))
game_logic.write_file(lines, position)
printer.print_rank(lines)
input("Wciśnij enter aby zakończyć program: ")
sys.exit()