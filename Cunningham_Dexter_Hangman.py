from WordGenerator import WordGenerator
from GameStatus import GameStatus


class Hangman():
    """ Class containing all of the information and methods required to run a game of hangman on the console.
    """

    def __init__(self, game_word):
        """ Create an instance on hangman class with a specific word to play against.

        Arguments:
            game_word {str} -- Word the player must guess when playing hangman.
        """

        self.GAME_WORD = game_word.lower()
        self.starred_word_list = [* "*" * len(self.GAME_WORD)]
        self.incorrect_guess_count = 0

    def user_guess(self):
        """ Takes console input from user to allow character guessing. On exception, default user guess is returned (" ").

        Returns:
            str -- The user inputted guess.
        """

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
        """Checks is user's character guess is in the game word and modifies game word list.

        Arguments:
            guess {str} -- User's guess.

        Returns:
            list -- Game word as list with guessed charaters inputted if guess valid.
        """

        correct_guess_indexes = [idx for idx, val in enumerate(
            self.GAME_WORD) if val == guess.lower()]

        if len(correct_guess_indexes) > 0:
            for idx in correct_guess_indexes:
                self.starred_word_list[idx] = guess.lower()
        else:
            self.incorrect_guess_count += 1

        return self.starred_word_list

    def get_starred_word_as_str(self, word_list):
        """Convert game word with user guesses to a str for output to user interface.

        Arguments:
            word_list {list} -- Game word split into characters with *s for hidden characters.

        Returns:
            list -- Game word plit into characters with *s for hidden characters with user's guess revealed.
        """

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
    """Holds logic for game loop
    """

    def __init__(self, hangman_game: Hangman):
        """Create instance of game engine to facilitate user interaction with system.

        Arguments:
            hangman_game {Hangman} -- Game class of type Hangman
        """

        self.game = hangman_game
        self.running_engine()

    def running_engine(self):
        """Continuous loop for game logic to allow user interaction with system. Loop will continue until game is won or lost.
        """

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
