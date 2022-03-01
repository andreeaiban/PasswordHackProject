# Brute Force Approach To guessing a User's Password
# The time complexity of brute force is O(m*n)
# So, if we were to search for a string of "n" characters in a string of "m"
# characters using brute force, it would take us n * m tries.

import random
import string

import pyautogui

# storing all possible characters & #'s
# chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# ANOTHER WAY: (includes all symbols too)
chars = string.printable

# concert all chars into a list
chars_list = list(chars)

# counter variable
count = 0
# get password from user using pyautogui
# (lets your Python scripts control the mouse and keyboard to automate interactions with other applications)
password = pyautogui.password("Enter a password: ")

# declare a variable to store the guessed password
curr_guess_pass = ""

# Loop through curr_guess_pass until it becomes the correct password

while(curr_guess_pass!=password):
    # random chars from char list with len of the actual password
    # must be 'k' for the choices method syntax that represents how long of a random char generated
    curr_guess_pass = random.choices(chars_list, k=len(password))
    # count each guess
    count += 1
    # guessed password display
    print("Brute Force Guess #" + str(count) +":" + str(curr_guess_pass))

    # if current password guess is = to the password then password is found and displayed
    if(curr_guess_pass == list(password)):
        print("Password found: " + str(curr_guess_pass))
        # stop loop
        break

# When this program is runs, you can tell by the number of guesses the program will make until a correct password
# Is every inefficient so in the future I wish to add to the password Hack class other ways to guess correctly
# 1. Dictionary attack slightly better than brute force b/c the use of commonly used words

