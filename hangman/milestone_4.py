import random


class Hangman:
    """

    Word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your
    script

    word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example,
    if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a',
    the list would be ['a', '_', '_', '_', '_']

    num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet

    num_lives: int - The number of lives the player has at the start of the game.

    word_list: list - A list of words

    list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

    """

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    """
    
    letter: guess letter in lowercase
    Function checks to see if guess is right
    
    """

    def check_guess(self, guess):
        letter = guess.lower()
        if letter in self.word:
            print(f"Good guess! {letter} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] == letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    """
    
    guess = User is asked to guess a letter
    Validation to check whether a letter has been entered
    
    """

    def ask_for_user_input(self):
        while True:
            guess = input("Enter your guess letter: ")
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
