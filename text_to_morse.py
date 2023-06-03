import os
from morse_class import Morse
from morse_art import logo
from time import sleep

def clear():
    # check and runs the command for the specific operating system
    command = 'clear' if os.name == 'posix' else 'cls'
    os.system(command)
def run_main_prog():
    clear()
    print(logo)
    text = input(
        'Enter text(Only letters and numbers from the american alphabet) '
        'and press Enter: \n'
    ).upper()
    morse = Morse(text)
    print(f'\nMORSE TEXT:\n{morse.morse_text}')
    run_again = input(
        '\nDo you wanna run the program again? (y/n): ').lower()
    end_program = True if run_again == 'n' else False
    if not end_program:
        run_main_prog()
    print('GOOD BYE...')
    sleep(3)
    clear()
    exit()

if __name__ == '__main__':
    run_main_prog()
