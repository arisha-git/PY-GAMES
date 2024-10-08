# Number Guessing Game

import random

# giving a limit till where the user is supposed to guess
top_of_range = input("Type a number limit: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

# condition to print a positive interger   
    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()
    

random_number = random.randint(0, top_of_range)
guesses = 0

# loop for guessing the number
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue

    if user_guess == random_number:
        print("You got it correct!")
        break
# hints for guessing the number
    else:
        if user_guess > random_number:
            print("Type a smaller number.")
        else:
            print("Type a larger number")

print("You got it in", guesses, "guesses")

# End of program
