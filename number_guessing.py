#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program lets users guess the number

import random


def main():
    # this function uses a try statement

    # input
    user_guess = input("Guess a number between 1-9: ")
    random_variable = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    try:
        user_guess = int(user_guess)
        print("You entered an integer correctly.")

    except ValueError:
        print("That was not an integer.")

    else:
        if user_guess == random_variable:
            print("You guessed the correct number!")
        else:
            print(
                "You guessed the wrong number! The number was "
                + str(random_variable)
                + "."
            )
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
