import argparse
import re

WIN = '勝ち'
LOSE = '負け'
FIRST = 0
LAST = -1
SMALL_WORDS = '[ぁぃぅぇぉゃゅょゎ]'
KANA_WORDS = '[ァ-ヴ]'
NG_WORD = 'ん'
ME = 'あなた' 
OPPONENT = '相手'
KANA_STR_CODE = -96
SMALL_STR_CODE = 1


def parser():
    parser = argparse.ArgumentParser(description='Process some integers')
    parser.add_argument('word_dictionary', help='word_dictionary')
    args = parser.parse_args()
    return args


def convert_word(before_word, words, str_code):
    word = ""
    for w in before_word:
        if re.match(words, w):
            w = ord(w) + str_code
            w = chr(w)
        word += w
    return word


class Player():
    words_log = []

    def __init__(self):
        self.word = ''
        self.lose = False

    def get_last_char(self):
        return self.word[LAST]

    def convert_simple_word(self):
        self.word = self.word.rstrip('ー')
        self.word = convert_word(self.word, KANA_WORDS, KANA_STR_CODE)
        self.word = convert_word(self.word, SMALL_WORDS, SMALL_STR_CODE)
        
    def get_word(self):
        self.word = input('言葉を入力して下さい: ')

    def append_words_log(self, word):
        self.words_log.append(word)

    def judge_word(self):
        if self.word[LAST] == NG_WORD or self.word in Player.words_log:
            self.lose = True
            print('lose')
        elif Player.words_log:
            if Player.words_log[LAST][LAST] != self.word[FIRST]:
                self.lose = True
                print('lose')

    def __str__(self):
        return "word:" + self.word


class Dictionary():
    def __init__(self):
        self.dict = {}

    def load_dictionary(self, dictionary):
        with open(dictionary, 'r') as fp:
            for word in fp:
                word = word.rstrip()
                self.dict[word] = word[FIRST]

    def get_answer_word(self, last_char):
        for word, first_char in self.dict.items():
            if first_char == last_char:
                return word
        return LOSE


def main():
    args = parser()
    me = Player()
    opponent = Player()
    dictionary = Dictionary()
    dictionary.load_dictionary(args.word_dictionary)
    while(me.lose!=True and opponent.lose!=True):
        me.get_word()
        print(me)
        me.convert_simple_word()
        me.judge_word()
        me.words_log.append(me.word)
        opponent.word = dictionary.get_answer_word(me.get_last_char())
        print(opponent)
        opponent.convert_simple_word()
        opponent.judge_word()
        opponent.words_log.append(opponent.word)


if __name__ == '__main__':
    main()
