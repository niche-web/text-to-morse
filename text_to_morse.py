from morse_class import Morse
from morse_art import logo

def run_main_prog():
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

if __name__ == '__main__':
    run_main_prog()
