import sys
import re

WIN = '勝ち'
LOSE = '負け'
LAST = -1

class Word():
    def __init__(self):
        self.word = ''
        self.words_log = []

    def get_last_char(self):
        return self.word[LAST]

    def convert_simple_word(self):
        self.word = re.compile(['ぁ'-'ゎ'], self.word)
        # TODO カタカナ変換, 長音記号変換
        return self.word

    def get_word(self):
        self.word = input('言葉を入力して下さい: ')
        self.words_log.append(self.word)

    def judge_word(self):
        # TODO 一度使ってないか,  前の単語としりとりが成立しているか
        if self.word[LAST] == 'ん':
            return False
        else:
            return True

class Dictionary():
    def __init__(self):
        self.dict = {}

    def make_dictionary(self, dictionary):
        with open(dictionary, 'r') as fp:
            for line in fp:
                line = line.rstrip()
                self.dict[line] = line[0]
                
    def get_answer_word(self, last_char):
        # TODO 被らないように考慮する必要あり
        for word, top in self.dict.items():
            if top == last_char:
                return word
        return LOSE

def main():
    word = Word()
    dictionary = Dictionary()
    dictionary.make_dictionary(sys.argv[1])
    while(True):
        word.get_word()
        if word.judge_word() == False:
            print(LOSE)
        answer = dictionary.get_answer_word(word.get_last_char())
        if answer == LOSE:
            print(LOSE)
    return

if __name__ == '__main__':
    main()
