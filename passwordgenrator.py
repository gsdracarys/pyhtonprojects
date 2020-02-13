import sys
import os
import random
import string

def check_int_valid(*args):
    errmsg = ""

    if not int(args[0]):
        errmsg = "Please enter only integers and greater than 0 \n"
        sys.exit()

    if args[1] < 6:
        errmsg = "Password should be greater thn 6"
        sys.exit()

    return errmsg

def genrate_password(len_password,num_letters,num_numbers):
    password_characters = generate_string(string.ascii_letters,num_letters) + generate_string(string.digits,num_numbers) + string.punctuation
    return password_characters

def generate_string(typechar,length):
    for i in range(length):
        generated_string = ''.join(typechar)
    return generated_string

def main():
    min_length = 6
    len_password = input("How many characters you want your password to be generated ?\n")
    check_int_valid(len_password,min_length)

    num_letters = input("How many letters do you want ?\n")
    check_int_valid(num_letters)

    num_numbers = input("How many numbers do you want ?\n")
    check_int_valid(num_numbers)

    print(genrate_password(len_password,num_letters,num_numbers))

if __name__ == "__main__":
    main()

