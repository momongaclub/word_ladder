import sys
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


class Word():

    words_log = []

    def __init__(self):
        self.word = ''

    def get_last_char(self):
        return self.word[LAST]

    def convert_simple_word(self):
        self.word = self.word.rstrip('ー')

        word = ""
        for w in self.word:
            if re.match(KANA_WORDS, w):
                w = ord(w) + KANA_STR_CODE
                w = chr(w)
            word += w
        self.word = word

        word = ""
        for w in self.word:
            if re.match(SMALL_WORDS, w):
                w = ord(w) + SMALL_STR_CODE
                w = chr(w)
            word += w
        self.word = word

    def get_word(self):
        self.word = input('言葉を入力して下さい: ')

    def append_words_log(self, word):
        self.words_log.append(word)

    def judge_word(self):
        if self.word[LAST] == NG_WORD or self.word in Word.words_log:
            return LOSE
        elif Word.words_log:
            if Word.words_log[LAST][LAST] != self.word[FIRST]:
                return LOSE


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
    me = Word()
    opponent = Word()
    dictionary = Dictionary()
    dictionary.load_dictionary(sys.argv[1])
    while(True):
        me.get_word()
        print(ME + me.word)
        me.convert_simple_word()
        print(me.word)
        if me.judge_word() == LOSE:
            print(ME + LOSE)
            break
        me.words_log.append(me.word)
        opponent.word = dictionary.get_answer_word(me.get_last_char())
        print(OPPONENT + opponent.word)
        opponent.convert_simple_word()
        if opponent.judge_word() == LOSE:
            print(OPPONENT + LOSE)
            break
        opponent.words_log.append(opponent.word)


if __name__ == '__main__':
    main()
