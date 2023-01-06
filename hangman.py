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
