import random

class Hangman:


    def __init__(self, word_list):
        """
        Initializes a Hangman game with a list of possible words.

        Parameters:
        word_list (list): A list of strings representing th possible words in the game.

        Attributes:
        word(str): The word to be guessed by the player.
        guesses (list): A list of letters that the player has guessed so far.
        num_guesses (int): The number of incorrect guesses allowed before the game is over.
        current_guesses (int): The number of incorrect guesses made by the player so far.
        display_word (str): The word as it appears to the player, with underscores representing unguessed letters.
        hangman_states (list): A list of art representations of the hangman as it is being drawn.
        """
        self.word_list = word_list
        self.word = ""
        self.guesses = []
        self.guesses_num = 6
        self.guesses_current = 0
        self.word_display = ""
        self.states_hangman = [
            """
             +---+
             |   |
                 |
                 |
                 |
                 |
            =========""",
            """
             +---+
             |   |
             O   |
                 |
                 |
                 |
            =========""",
            """
             +---+
             |   |
             O   |
             |   |
                 |
                 |
            =========""",
            """
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
            =========""",
            """
             +---+
             |   |
             O   |
            /|\\  |
                 |
                 |
            =========""",
            """
             +---+
             |   |
             O   |
            /|\\  |
            /    |
                 |
            =========""",
            """
             +---+
             |   |
             O   |
            /|\\  |
            / \\  |
                 |
            ========="""
        ]
