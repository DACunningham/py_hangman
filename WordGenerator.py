from random import randint


class WordGenerator():

    def __init__(self):
        pass

    def open_words_txt(self, location):
        try:
            temp_text = open(location)
        except OSError as ex:
            print(
                f"C err no#: {ex.errno}\nError message: {ex.strerror}\nPath passed in: {ex.filename}")
        else:
            return temp_text.read().splitlines()
        finally:
            temp_text.close()

    def get_random_word(self, words):
        rand_word_index = randint(0, (len(words) - 1))
        return words[rand_word_index]
