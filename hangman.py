from WordGenerator import WordGenerator
from GameStatus import GameStatus


class Hangman():

    def __init__(self, game_word):
        self.GAME_WORD = game_word.lower()
        self.starred_word_list = [* "*" * len(self.GAME_WORD)]
        self.incorrect_guess_count = 0

    def user_guess(self):
        _user_input = ""
        try:
            _user_input = input(f"\nIncorrect Guesses: {self.incorrect_guess_count} of 7." +
                                f"\nThe word to be guessed is: {self.get_starred_word_as_str(self.starred_word_list)}" +
                                "\nPlease enter your next guess: ")
        except EOFError as ex:
            # Logging here. Not required for task
            # input set to space as bad character sent to program, invalid guess.
            _user_input = " "
        finally:
            return _user_input

    def user_guess_valid(self, guess):
        correct_guess_indexes = [idx for idx, val in enumerate(
            self.GAME_WORD) if val == guess.lower()]

        if len(correct_guess_indexes) > 0:
            for idx in correct_guess_indexes:
                self.starred_word_list[idx] = guess.lower()
        else:
            self.incorrect_guess_count += 1

        return self.starred_word_list

    def get_starred_word_as_str(self, word_list):
        return "".join(self.starred_word_list)

    def check_game_success(self, starred_word_list, incorrect_guess_count):
        """ Checks to see if 7 incorrect guesses have been made or the word has been correctly guessed.

        Arguments:
            starred_word_list {list} -- A list of chars representing the game word as the user should see it.
            incorrect_guess_count {int} -- A count of how many incorrect guesses the user has made so far.

        Returns:
            [GameStatus] -- Appropriate enum describing the current status of the game based on user input.
        """

        if incorrect_guess_count > 7:
            return GameStatus.game_lost
        elif starred_word_list.count("*") == 0:
            return GameStatus.game_won
        else:
            return GameStatus.game_in_progress


class GameEngine():

    def __init__(self, hangman_game: Hangman):
        self.game = hangman_game
        self.running_engine()

    def running_engine(self):

        game_status = GameStatus.game_in_progress
        while game_status == GameStatus.game_in_progress:
            user_input = self.game.user_guess()
            self.game.starred_word_list = self.game.user_guess_valid(
                user_input)
            game_status = self.game.check_game_success(
                self.game.starred_word_list, self.game.incorrect_guess_count)

        if game_status == game_status.game_won:
            print("Congratulations you win!")
        else:
            print("You lose!")


if __name__ == "__main__":
    word_generator = WordGenerator()
    words = word_generator.open_words_txt("words.txt")
    rand_word = word_generator.get_random_word(words)
    game = Hangman(rand_word)
    engine = GameEngine(game)
