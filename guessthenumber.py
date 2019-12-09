# Guess the number
import os
import sys
import random

def main():
    rand_num = 0
    rand_num = random_num()
    number = inputnum()

    while number != rand_num:
        if number < rand_num:
            print("Your guess is smaller than number")
        elif number > rand_num:
            print("Your guess is greater than number")
        number = inputnum()

    if number == rand_num:
        print("Bang on !! {} is right answer".format(number))


def inputnum():
    number = input("Please enter your guess - ")
    return number

def random_num():
    rand_num = random.randint(0, 20)
    return rand_num

if __name__ == "__main__":
    main()