Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... words = ["python", "hangman", "programming", "developer"]
... word = random.choice(words)
... guessed_letters = set()
... attempts = 6
... 
... while attempts > 0:
...     display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
...     print(f"Word: {display} | Attempts left: {attempts}")
...     
...     guess = input("Guess a letter: ").lower()
...     
...     if guess in guessed_letters:
...         print("You've already guessed that letter.")
...         continue
... 
...     guessed_letters.add(guess)
... 
...     if guess in word:
...         print("Good guess!")
...     else:
...         attempts -= 1
...         print("Wrong guess!")
... 
...     if all(letter in guessed_letters for letter in word):
...         print(f"Congratulations! You've guessed the word: {word}")
...         break
... else:
...     print(f"Game Over! The word was: {word}")
