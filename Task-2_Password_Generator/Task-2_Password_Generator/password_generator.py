# Random Password Generator
# Oasis Infobyte Python Development Internship
# Author: Nandini Gaikwad

import random
import string

print("----- Random Password Generator -----")

try:
    length = int(input("Enter desired password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")
