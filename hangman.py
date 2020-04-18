from WordGenerator import WordGenerator
from GameStatus import GameStatus


class Hangman():

    def __init__(self, game_word):
        self.GAME_WORD = game_word.lower()
        self.starred_word_list = [*"*"*len(self.GAME_WORD)]

    def user_guess(self):
        return input("Please enter your next guess: ")

    def user_guess_valid(self, guess):
        correct_guess_indexes = [idx for idx, val in enumerate(
            self.GAME_WORD) if val == guess.lower()]

        if len(correct_guess_indexes) > 0:
            for idx in correct_guess_indexes:
                self.starred_word_list[idx] = guess.lower()

        return self.starred_word_list

    def get_starred_word_as_str(self, word_list):
        return "".join(self.starred_word_list)

    def check_game_success(self, starred_word_list, incorrect_guess_count):
        if incorrect_guess_count > 7:
            return GameStatus.game_lost
        elif starred_word_list.count("*") == 0:
            return GameStatus.game_won
        else:
            return GameStatus.game_in_progress


if __name__ == "__main__":
    word_generator = WordGenerator()
    words = word_generator.open_words_txt("words.txt")
    rand_word = word_generator.get_random_word(words)
    game = Hangman(rand_word)
