import sys
import re

WIN = '勝ち'
LOSE = '負け'
FIRST = 0
LAST = -1
SMALL_WORDS = '[ぁぃぅぇぉゃゅょゎ]'
NG_WORD = 'ん'

class Word():
    def __init__(self):
        self.word = ''
        self.words_log = []

    def get_last_char(self):
        return self.word[LAST]

    def convert_simple_word(self):
        self.word = self.word.rstrip('ー')
        # カタカナ変換
        # 小文字変換 今の文字に対してプラス1する
        #for i in range(0, len(self.word)):
        #    self.word[i] = re.sub(SMALL_WORDS, self.word[i]+1, self.word[i])
        print(self.word)

    def get_word(self):
        self.word = input('言葉を入力して下さい: ')

    def append_words_log(self, word):
        self.words_log.append(word)

    def judge_word(self):
        if self.word[LAST] == NG_WORD or self.word in self.words_log:
            return LOSE
        elif self.words_log:
            if self.words_log[LAST][LAST] != self.word[FIRST]:
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
    word = Word()
    dictionary = Dictionary()
    dictionary.load_dictionary(sys.argv[1])
    while(True):
        word.get_word()
        if word.judge_word() == LOSE:
            print(LOSE)
            break
        word.convert_simple_word()
        word.append_words_log(word.word)
        print('自分：' + word.word)
        answer = dictionary.get_answer_word(word.get_last_char())
        # TODO 相手のwordもconvertする必要がある
        print('相手：' + answer)
        if answer == LOSE:
            break
        word.append_words_log(answer)
    return

if __name__ == '__main__':
    main()
