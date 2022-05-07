from numpy import *
from termcolor import colored
import os,time
import pandas as pd
import game_logic

def printer(game_table, pad_size,block_position):
    os.system('clear')
    s = int(len(game_table))
    c =[]
    for j in range(int(len(game_table))):
        c.append(["white"] * 20)

    for z in range(len(block_position)):
        c[int(block_position[z][0])][int(block_position[z][1])]="red"

    for u in range(len(pad_size)):
        c[int(pad_size[u][0])][int(pad_size[u][1])]="green"


    header = "   ╔"
    for i in range(s - 1):
        header = header + "═╦"
    header = header + "═╗"

    body = "   ╠"
    for i in range(s - 1):
        body = body + "═╬"
    body = body + "═╣"

    base = "  ╚"
    for i in range(s - 1):
        base = base + "═╩"
    base = base + "═╝"


    print("   ", end=" ")
    for i in range(s):
        print(i + 1, end=" ")
    print("\n", header,)
    for i in range(s):
        if i < 9:
            print(i+1, "  ", end="║")
        if i >= 9:
            print(i + 1, " ", end="║")
        for j in range(s):
            print(colored(str(game_table[i][j]), str(c[i][j])), end="║")

        if i != s-1:
            print("\n", body)
        else:
            print("\n ", base)


def print_gameStatus(min, sec, moves_counter, point_counter):
    string1 = "Twój aktualny czas to " + str(int(min)) + ":" + str(int(sec))
    string2 = ", a twój aktualny wynik to: " + str(round(game_logic.score(moves_counter, min, point_counter),1)) + " puntków"
    print(string1 + string2, end = "\r")


def print_rank(lines):
    os.system('clear')
    wyniki = lines['Wynik'].tolist()
    nazwy = lines['Nazwa'].tolist()
    ruchy = lines['LiczbaRuchów'].tolist()
    minuty = lines['Minuty'].tolist()
    sekundy = lines['Sekundy'].tolist()
    width = 1 + max_len(wyniki, "wyniki") + 3 + max_len(nazwy, "Nazwa") + 3 + max_len(ruchy, "Liczba ruchów") +3 + 8
    print("\n" + "*" * width)
    print("*" + " " * (max_len(wyniki, "wyniki") + 2) + "*" + " " * (max_len(nazwy, "Nazwa") + 2) + "*" + " " *
          (max_len(ruchy, "Liczba ruchów") + 2) + "*" + " " * 7 + "*")
    where_center("Wynik", max_len(wyniki, "wyniki") + 2)
    where_center("Nazwa", max_len(nazwy, "Nazwa") + 2)
    where_center("Liczba Ruchów", max_len(ruchy, "Liczba Ruchów") + 2)
    where_center("Czas", 7)
    print("*")
    print("*" + " " * (max_len(wyniki, "wyniki") + 2) + "*" + " " * (max_len(nazwy, "Nazwa") + 2) + "*" + " " *
          (max_len(ruchy, "Liczba ruchów") + 2) + "*" + " " * 7 + "*")
    print("*" * width)
    for i in range(len(wyniki)):
        if i <8:
            printing_rank_position(wyniki, nazwy, ruchy, minuty, sekundy, i, width)


def max_len(list, name):
    lenght = len(name)
    for i in range(len(list)):
        if len(str(list[i]))>lenght:
            lenght = len(str(list[i]))

    return lenght


def where_center(string, lenght):
    div = lenght - len(string)
    print("*",end="")
    if div%2 == 0:
        hm = int(div/2)
        print(" " * hm+string+" "* hm, end = "")
    elif div%2 == 1:
        hm = int((div-1)/2)
        hm2 = int(hm)+1
        print(" " * hm2 + string + " " * hm, end="")


def printing_rank_position(list1,list2,list3,list4,list5,i,width):
    print("*" + " " * (max_len(list1, "wyniki") + 2) + "*" + " " * (max_len(list2, "Nazwa") + 2) + "*" + " " *
          (max_len(list3, "Liczba ruchów") + 2) + "*" + " " * 7 + "*")
    where_center(str(list1[i]), max_len(list1, "wyniki") + 2)
    where_center(str(list2[i]), max_len(list2, "Nazwa") + 2)
    where_center(str(list3[i]), max_len(list3, "Liczba Ruchów") + 2)
    date = str(list4[i]) + ":" + str(list5[i])
    where_center(date, 7)
    print("*")
    print("*" + " " * (max_len(list1, "wyniki") + 2) + "*" + " " * (max_len(list2, "Nazwa") + 2) + "*" + " " *
          (max_len(list3, "Liczba ruchów") + 2) + "*" + " " * 7 + "*")
    print("*" * width)


def choice_menu(ch, position):
    if ch == 'd':
        position = position + 1
    if ch == 'a':
        position = position - 1

    if position == 4:
        position = 0
    elif position == -1:
        position = 3
    return position


def print_menu(position):
    colors = ['white','white','white','white']
    text = ['ŁATWY','ŚREDNI','TRUDNY','SUPER-TRUDNY']
    colors[position] = 'green'
    os.system('clear')
    print('*'* 91)
    print('*',' '*87, '*')
    print('*', ' ' * 87, '*')
    print('*','  ',colored('*' * 15,str(colors[0])),'  ',colored('*'* 17, str(colors[1])) ,'  ',
          colored('*'* 17,str(colors[2])),'  ',colored('*'*22,str(colors[3])) ,'','*')
    print('*','  ',colored('*',colors[0]), ' '*(len(text[0])+6),colored('*',colors[0])
          ,'  ',colored('*',colors[1]), ' '*(len(text[1])+7),colored('*',colors[1])
          ,'  ',colored('*',colors[2]), ' '*(len(text[2])+7),colored('*',colors[2]),
          '  ',colored('*',colors[3]), ' '*(len(text[3])+6),colored('*',colors[3]),'','*' )
    print('*','  ',colored('*',colors[0]),'  ',colored(text[0],colors[0]),'  ',colored('*',colors[0]),'  ',
          colored('*',colors[1]),'  ',colored(text[1],colors[1]),'   ',colored('*',colors[1]),'  ',colored('*',colors[2])
          ,'  ',colored(text[2],colors[2]),'   ',colored('*',colors[2]),'  ',colored('*',colors[3]),
          '  ',colored(text[3],colors[3]),'  ',colored('*',colors[3]),'','*' )
    print('*', '  ', colored('*', colors[0]), ' ' * (len(text[0]) + 6), colored('*', colors[0])
          , '  ', colored('*', colors[1]), ' ' * (len(text[1]) + 7), colored('*', colors[1])
          , '  ', colored('*', colors[2]), ' ' * (len(text[2]) + 7), colored('*', colors[2]),
          '  ', colored('*', colors[3]), ' ' * (len(text[3]) + 6), colored('*', colors[3]), '', '*')
    print('*','  ',colored('*' * 15,str(colors[0])),'  ',colored('*'* 17, str(colors[1])) ,'  ',
          colored('*'* 17,str(colors[2])),'  ',colored('*'*22,str(colors[3])) ,'','*')
    print('*', ' ' * 87, '*')
    print('*', ' ' * 87, '*')
    print('*' * 91)



