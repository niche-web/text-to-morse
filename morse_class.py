import csv
# import winsound

# TIME_UNIT = 50  # in milliseconds
# FREQ = 10000  # in hertz
# SOUND_ARG = {
#     '.': (FREQ, TIME_UNIT),
#     '-': (FREQ, TIME_UNIT * 3),
#     '*': (50, TIME_UNIT)
# }


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

    def convert_word(self, word_to_convert, inter_symbol=False):
        letter_morse_list = ['*'.join(list(self.letter_dict[letter]))
                             if inter_symbol
                             else self.letter_dict[letter]
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

    # def play(self):
    #     for elem in self.morse_text_track:
    #         winsound.Beep(*SOUND_ARG[elem])

    # TODO 2. Convert letter to morse (letters/numbers, space between words).
    #   dit = 1 * TIME_UNIT / FREQ
    #   dah = 3 * TIME_UNIT / FREQ
    #   inter_element = 1 * TIME_UNIT(mute)
    #   between_letters = 3 * inter_element
    #   between_words = 7 * inter_element






