# func.py file belongs to PyPassV

# version-control and matching
PyPassV_version = 0.1

# import libs
import os, time, colorama

# set colors
c_green = colorama.Fore.GREEN
c_red = colorama.Fore.RED
c_reset = colorama.Fore.RESET

# set shell-logging icons with colors
log_neutral = '[>]'
log_positive = f'{c_green}[+]{c_reset}'
log_negative = f'{c_red}[-]{c_reset}'


# since the 'hide_cursor' carries over after exit, this setup makes it visible before exiting
def custom_exit():
    show_cursor()
    exit()


# hiding the cursor, good for string-prints where the cursor does not need to be seen
def hide_cursor():
    print('\033[?25l', end='')


# shows the cursor again when neccessary, need to be used before exit since the 'hide' command carries over after exit
def show_cursor():
    print('\033[?25h', end='')


# clear the shell, for when "end=' \r'" is not used
def clear_shell():

    """cleaning the shell from top to bottom"""

    if os.name == 'nt': # 'nt' is what Windows uses to identify it's os-type
        os.system('cls')
    else:
        os.system('clear')


def wipe_line(repeat = None): # 'repeat = None' makes the argument 'repeat' valid, even when no value is passed

    """using ASCII keycodes to manipulate shell-strings, in this case, removing them"""

    if repeat == 1 or repeat == None:
        print('\033[K', end=' \r')
    else:
        for i in range(0, repeat):
            print('\033[A' + '\033[K', end=' \r') # keycode '\033[A' moves cursor up, '\033[K' removed the active/current line/string


def input_sanetizer(input):

    input = str(input)
    input = input.strip()

    valid_input_characters = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if input.lower() == 'q':
        return exit()
    if len(input) >= 50:
        return False
    for i in input:
        if i not in valid_input_characters:
            return False
    else:
        return True