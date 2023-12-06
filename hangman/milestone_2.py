import random

word_list = ["apple", "banana", "strawberries", "watermelon", "orange"]
word = random.choice(word_list)
guess = input("Please enter a letter:\n")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good Guess!")
else:
    print("Oops!")
