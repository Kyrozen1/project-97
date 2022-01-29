import random
number = random.randint(1,9)
chances = 0
print(number)
print("number guessing game")
print("Guess a number between 1 and 9")

while chances<5:
    guess = int(input("enter your guess:"))
    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    elif guess != number:
        print("Incorrect, try guessing a different number")
        chances = chances+1
if not chances < 5:
    print("YOU LOSE!!! The number is", number)