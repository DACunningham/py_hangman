import unittest
from unittest.mock import patch
import os
from Hangman import Hangman
from GameStatus import GameStatus
from WordGenerator import WordGenerator


class WordGeneratorTests(unittest.TestCase):

    def test_open_words_file_success(self):
        # Arrange
        temp_txt = open("temp.txt", "w+")
        temp_txt.write("Dexter\n")
        temp_txt.write("Cunningham\n")
        temp_txt.close()
        location = "temp.txt"
        word_gen = WordGenerator(location)

        # Act
        words = word_gen.open_words_txt(location)

        # Assert
        self.assertListEqual(words, ["Dexter", "Cunningham"])

        # Clean
        os.remove(location)

    def test_get_game_word(self):
        # Arrange
        temp_txt = open("temp.txt", "w+")
        temp_txt.write("Dexter")
        temp_txt.write("Cunningham")
        temp_txt.close()
        location = "temp.txt"
        word_gen = WordGenerator(location)
        words = word_gen.open_words_txt(location)

        # Act
        word = word_gen.get_random_word(words)

        # Assert
        self.assertIn(word, ["Dexter", "Cunningham"])

        # Clean
        os.remove(location)


class HangmanGameTests(unittest.TestCase):

    @patch('builtins.input', lambda *args: 'e')
    def test_get_user_guess_input_success(self):
        # Arrange
        hangman = Hangman()

        # Act
        result = hangman.user_guess()

        # Assert
        self.assertEqual(result, "e")

    def test_check_guess_validity(self):
        # Arrange
        hangman = Hangman()
        guess = "e"
        WORD = "Dexter"
        word_list = [*"*"*len(WORD)]
        word_list[1] = "e"
        word_list[4] = "e"

        # Act
        result = hangman.user_guess_valid(guess)

        # Assert
        self.assertListEqual(result, word_list)

    def test_get_starred_word_string(self):
        # Arrange
        hangman = Hangman()
        WORD = "Dexter"
        word_list = [*"*"*len(WORD)]
        word_list[1] = "e"
        word_list[4] = "e"

        # Act
        result = hangman.get_starred_word_as_str(word_list)

        # Assert
        self.assertEqual(result, "*e**e*")

    def test_check_game_success_word_guessed(self):
        # Arrange
        hangman = Hangman()
        WORD = "Dexter"
        word_list = [*WORD]
        guess_count = 0

        # Act
        result = hangman.check_game_success(word_list, guess_count)

        # Assert
        self.assertEqual(result, GameStatus.success)

    def test_check_game_success_word_not_guessed(self, word_dict, guess_count):
        # Arrange
        hangman = Hangman()
        WORD = "Dexter"
        word_list = [*"*"*len(WORD)]
        word_list[1] = "e"
        word_list[4] = "e"
        guess_count = 0

        # Act
        result = hangman.check_game_success(word_list, guess_count)

        # Assert
        self.assertEqual(result, GameStatus.still_playing)

    def test_check_game_success_max_guesses_exceeded(self, word_dict, guess_count):
        # Arrange
        hangman = Hangman()
        WORD = "Dexter"
        word_list = [*"*"*len(WORD)]
        word_list[1] = "e"
        word_list[4] = "e"
        guess_count = 8

        # Act
        result = hangman.check_game_success(word_list, guess_count)

        # Assert
        self.assertEqual(result, GameStatus.game_over)


if __name__ == "__main__":
    unittest.main()
