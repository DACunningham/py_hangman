from WordGenerator import WordGenerator


class Hangman():

    def __init__(self, game_word):
        self.GAME_WORD = game_word
        self.starred_word_list = [*"*"*len(self.GAME_WORD)]

    def user_guess(self):
        return input("Please enter your next guess: ")

    def user_guess_valid(self, guess):
        correct_guess_indexes = [idx for idx, val in enumerate(
            self.GAME_WORD) if val == guess]

        if len(correct_guess_indexes) > 0:
            for idx in correct_guess_indexes:
                self.starred_word_list[idx] = guess

        return self.starred_word_list


if __name__ == "__main__":
    word_generator = WordGenerator()
    words = word_generator.open_words_txt("words.txt")
    rand_word = word_generator.get_random_word(words)
    game = Hangman(rand_word)
