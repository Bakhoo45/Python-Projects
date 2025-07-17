#number guessing games

import random

lowest_number = 1
highest_number = 100
number_to_guess = random.randint(lowest_number, highest_number)
number_of_guesses = 0

while True:
    user_guess = int(input(f"Guess a number between {lowest_number} and {highest_number}: "))
    number_of_guesses += 1
    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number in {number_of_guesses} tries.")
        break
