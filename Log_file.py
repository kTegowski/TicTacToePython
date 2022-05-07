import os, time, sys
import pyfiglet
import os
from termcolor import colored


def print_log():
    os.system('clear')
    ascii_banner = pyfiglet.figlet_format("TIK TAK TOE")
    for char in ascii_banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    name = "by Konrad Tęgowski"
    space = " "
    for char in (53 - len(name)) * space:
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(1)
    os.system('clear')

def print_win():
    os.system('clear')
    ascii_banner = pyfiglet.figlet_format("WYGRAŁEŚ")
    for char in ascii_banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


def print_rules():
    os.system('clear')
    print("Zasady gry: ")
    print("Po planszy poruszamy się przyciskami", colored('WSAD', 'red'))
    print("Zmiany akcpetujemy", colored('ENTEREM','red'))
    print("Gra kończy się wraz z zapełnieniem całej planszy",colored('+','green'))
    print("Aby przerwać grę, zapisując swój wynik należy nacisnąc", colored('R','red'))
    input(colored('Aby przejśc dalej naciśnij ENTER', 'green'))
