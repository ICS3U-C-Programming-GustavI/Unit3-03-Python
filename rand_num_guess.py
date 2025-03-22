#!/usr/bin/env python3
# Created by: Gustav I
# Created on: March 18, 2025
# This program executes a number guessing game.

import random


def main():
    number_guess = int(input("Guess a number (0-9): "))
    print("")

    chosen_number = random.randint(0, 9)

    if number_guess == chosen_number:
        print("You guessed correct!")
    else:
        print(f"You guessed wrong! The correct answer was: {chosen_number}")


if __name__ == "__main__":
    main()
