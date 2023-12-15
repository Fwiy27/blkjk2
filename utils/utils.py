import sys
from os import system

def clear_screen():
    if sys.platform.startswith('win'):
        system('cls')
    else:
        system('clear')