import random

word_list = ["apple", "banana", "strawberries", "watermelon", "orange"]
word = random.choice(word_list)
flag = True
print(word)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Guess the letter:\n")
        if guess.isalpha():
            check_guess(guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


ask_for_input()
