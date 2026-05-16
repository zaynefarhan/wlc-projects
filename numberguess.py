# 1) choose a number
# 2) ask the user for an input
# 3) check if number is higher or lower and print

import random
randomNumber = random.randint(1,100)
count = 0

guess = ""

while randomNumber != guess:
    guess = int(input("Guess a number: "))
    if randomNumber > guess:
        print("Too low")
        count += 1
    elif randomNumber < guess:
        print("Too high")
        count += 1
    else:
        print("CORRECT")
        count += 1
        break

print(f"Guesses: {count}")
