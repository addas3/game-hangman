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

    def intro(self):
        """
        Write a welcoem message to the user when starting the game.
        """
        print("Welcome to Hangman Game!")
        print("Guess the word before the hangman is fully drawn.")
        print("Remember you have 6 guesses only.")
        print("Quick Hint: think about fruites.")
        print("Good Luck!!")
        print("\n")

    def word_choose(self):
        """
        Chooses a word at random from the list of possible words and initializes the display_word attribute.
        """
        self.word = random.choice(self.word_list)
        self.word_display = "_" * len(self.word)

    def guess(self):
        """
        Gets a guess from the player and update the word_display and guesses attributes based on the guess.
        """
        guess = input("Guess a letter: ")
        if guess in self.guesses:
            print("You have already guessed that letter. Try again.")
        else:
            self.guesses.append(guess)
            if guess in self.word:
                for i in range(len(self.word)):
                    if guess == self.word[i]:
                        self.word_display = self.word_display[:i] + guess + self.word_display[i+1:]
                print(f"Correct Answer! {self.word_display}")
            else:
                self.guesses_current += 1
                print(f"Incorrect Answer. you have {self.guesses_num - self.guesses_current} guesses left.")
                print(self.states_hangman[self.guesses_current])
                print(self.word_display)
    
    def play(self):
        """
        Plays a game of Hangman. Calls the intro, word_choose, and guess methods untill the game is won or lost.
        Asks the player if they want to play again after the game is over.
        """
        while True:
            self.intro()
            self.word_choose()
            while True:
                self.guess()
                if self.guesses_current == self.guesses_num:
                    print("Soory you lost! The word was", self.word)
                    break
                elif self.word_display == self.word:
                    print("WOOW Congratulations! You guessed the word!")
                    break
            print("\n")  # create a space before the prompt for the player to play again
            play_again = input("Do you want to give your self another try? (y/n):")
            if play_again.lower() != "y":
                break
    

word_list = [ 'apple',
    'banana', 
    'blackberry', 
    'cherry', 
    'lemon', 
    'kiwi', 
    'orange', 
    'grapes', 
    'lime', 
    'mango', 
    'peach',
    'pineapple',
    'raisins',
    'strawberry',
    'watermelon']
game = Hangman(word_list)
game.play()


