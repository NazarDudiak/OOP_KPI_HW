import re


class TextInfo:
    def __init__(self, input_filename):
        self.filename = input_filename

    def print_text(self):
        print("\nOur text:")
        with open(self.filename, "r") as fp:
            text = fp.read().splitlines()
            for sentence in text:
                print("\t" + sentence)

    def file_info(self):
        with open(self.filename, "r") as fp:
            print("\nFile data:")
            print('\tIs Closed:', fp.closed)
            print('\tEncoding Used:', fp.encoding)
            print('\tAccess Mode:', fp.mode)
            print('\tNewLines Found:', fp.newlines)

    def text_info(self):
        print("\nText info:")
        with open(self.filename, "r") as fp:
            text = fp.read().splitlines()
            max_len = 0
            words_length = 0
            sentences_length = 0
            for sentence in text:
                max_len += len(sentence)
                one_of_sentence = re.split(r"[\s,.!?-]", sentence)
                while "" in one_of_sentence:
                    one_of_sentence.remove("")
                words_length += len(one_of_sentence)
                sentences_length += 1
        print("\tСharacters in total:", max_len)
        print("\tTotal number of words:", words_length)
        print("\tTotal number of sentences:", sentences_length)

    pass


filename = input("Enter filename: ")
word = TextInfo(filename)
word.print_text()
word.file_info()
word.text_info()
