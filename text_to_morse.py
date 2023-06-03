import os
from time import sleep
from morse_class import Morse, MorseError
from morse_art import logo

def clear(message=None):
    # check and runs the command for the specific operating system
    command = 'clear' if os.name == 'posix' else 'cls'
    if message:
        print(message)
        sleep(3)
    os.system(command)

def stop(message):
    print(message)
    sleep(3)
    clear()
    exit()
def run_main_prog():
    end_program = False
    clear()
    print(logo)
    try:
        text = input(
            'Enter text(Only letters and numbers from the american alphabet) '
            'and press Enter: \n'
        ).upper()
        assert(text.strip())
    except AssertionError:
        print('No text to code...')
        clear('Try again...')
    except KeyboardInterrupt:
        stop('GOOD BYE ...')
    else:
        try:
            morse = Morse(text)
            print(f'\nMORSE TEXT:\n{morse.morse_text}')
            run_again = input(
                '\nDo you wanna run the program again? (y/n): ').lower()
        except MorseError as m:
            print(m)
            print('Only letters and numbers from the american alphabet')
            clear('Try again ...')
        except KeyboardInterrupt:
            stop('GOOD BYE...')
        else:
            end_program = True if run_again == 'n' else False

    if not end_program:
        run_main_prog()
    stop('GOOD BYE...')

if __name__ == '__main__':
    run_main_prog()
