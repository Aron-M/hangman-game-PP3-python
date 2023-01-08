import random

hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / 
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / \
"""
]

words = ['balloon', 'aeroplane', 'computer', 'corridor', 'television', 'university', 'paraglide', 'submarine', 'ferriswheel']

word = random.choice(words).lower()


guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = -1

while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_'
    if output == word:
        break
    print("Try to guess the correct word: ",output)
    print("You have ", tries," chances left")
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("You have already guessed", guess, " ,please try again!")