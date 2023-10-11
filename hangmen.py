import os
import random

from words import word_list


def gallows_body():
  print("______")
  print("|    |")
  if tries == 8:
    print("|")
    print("|")
    print("|")
    print("|")
  elif tries == 7:
    print("|    o")
    print("|")
    print("|")
    print("|")
  elif tries == 6:
    print("|    o")
    print("|    |")
    print("|")
    print("|")
  elif tries == 5:
    print("|    o")
    print("|    |")
    print("|   /")
    print("|")
  elif tries == 4:
    print("|    o")
    print("|    |")
    print("|   / \\")
    print("|")
  elif tries == 3:
    print("|    o")
    print("|   /|")
    print("|   / \\")
    print("|")
  elif tries == 2:
    print("|    o")
    print("|   /|\\")
    print("|   / \\")
    print("|")
  elif tries == 1:
    print("|    o")
    print("|   /|\\")
    print("|   / \\")
    print("|  -")
  elif tries == 0:
    print("|    o")
    print("|   /|\\")
    print("|   / \\")
    print("|  -   -")
  print("----")

terminal_height = os.get_terminal_size().lines

while True:
  word = random.choice(word_list)
  
  already_guessed = []
  incorrect_letters = []
  correct_letters = [" "] * len(word)

  tries = 8

  while True:
    print("\n" * terminal_height)

    print("\nIncorrect letters: ", end="")
    for letter in incorrect_letters:
      print(letter, end=" ")
    print()
    gallows_body()
    for letter in correct_letters:
      print(letter, end=" ")
    print()
    print("- " * len(word))

    if " " not in correct_letters:
      print("You win!")
      break
    elif tries == 0:
      print(f"You lose. The word was: {word}")
      break

    while True:
      guess = input("\nEnter a letter: ")

      if not guess.isalpha():
        print("Please enter a letter.")
        continue
      elif len(guess) > 1:
        print("Please enter only one letter.")
        continue
      elif guess in already_guessed:
        print("You already guessed that letter!")
        continue

      already_guessed.append(guess)
      break

    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          correct_letters[i] = guess
    else:
      tries -= 1
      incorrect_letters.append(guess)

  answer = input("Do you want to play again? ")
  if answer.startswith("n"):
    break
