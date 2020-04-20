from random import randint


class WordGenerator():
    """Class to provide implementations to open text file and select a random word.
    """

    def __init__(self):
        pass

    def open_words_txt(self, location):
        """Safely opens a text file and returns all of the words in a list.

        Arguments:
            location {str} -- Location of file ot open.

        Returns:
            list -- Words in opened file.
        """

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
        """Gets a word randomly from inputted list.

        Arguments:
            words {list} -- Words to be selected from.

        Returns:
            str -- A raondomly selected word.
        """

        rand_word_index = randint(0, (len(words) - 1))
        return words[rand_word_index]
