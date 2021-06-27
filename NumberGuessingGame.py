import random

print("Hello! In this game, the computer chooses a number between 1 and 10")
print("and you have to guess it. You have 5 chances. Can you guess the number?")
print("If you do not enter a number, the game will not work.")
number = random.randint(1,10)
chances = 5
while chances > 0:
  print("You have " + str(chances) + " chance(s) left.")
  guess = int(input("Enter your guess: "))

  if guess > number:
    print("Your guess was greater than the number.")
  
  if guess < number:
    print("You guess was smaller than the number.")

  if guess == number:
    print("YOU HAVE GUESSED THE NUMBER! GOOD JOB!")
    break

  chances = chances - 1

if chances == 0:
  print("You lost the game. Better luck next time.")