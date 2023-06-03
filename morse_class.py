import csv

class MorseError(Exception):
    pass

class Morse:
    def __init__(self, text):
        self.text = text.strip()
        self.letter_dict = Morse.create_letters_dict()
        self.morse_text = self.convert_text()
        self.morse_text_track = self.convert_text(inter_word=True)

    @staticmethod
    def create_letters_dict():
        letter_morse_dict = {}
        with open('morse.csv', newline='') as csv_file:
            letter_morse = csv.DictReader(csv_file)
            for row in letter_morse:
                letter_morse_dict[row['Letter']] = row['Code']
        return letter_morse_dict

    def code_symbol(self, letter):
        try:
            symbol = self.letter_dict[letter]
        except KeyError:
            raise(MorseError(f'[{letter}] --> Wrong character'))
        return symbol

    def convert_word(self, word_to_convert, inter_symbol=False):
        letter_morse_list = ['*'.join(list(self.code_symbol(letter)))
                             if inter_symbol
                             else self.code_symbol(letter)
                             for letter
                             in word_to_convert]
        if inter_symbol:
            return '***'.join(letter_morse_list)
        return ' '.join(letter_morse_list)

    def convert_text(self, inter_word=False):
        word_morse_list = [self.convert_word(word, inter_symbol=inter_word)
                           for word
                           in self.text.split()]
        if inter_word:
            return '*******'.join(word_morse_list)
        return ' / '.join(word_morse_list)  # 3 spaces for inter-word








