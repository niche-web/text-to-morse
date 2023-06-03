from morse_class import Morse


def run_main_prog():
    text = input(
        'Enter text(Only letters and numbers from the american alphabet) '
        'and press Enter: \n'
    ).upper()
    morse = Morse(text)
    print(f'\nMORSE TEXT:\n{morse.morse_text}')

if __name__ == '__main__':
    end_program = False
    while not end_program:
        run_main_prog()
        run_again = input('\nDo you wanna run the program again? (y/n): ').lower()
        end_program = True if run_again == 'n' else False






