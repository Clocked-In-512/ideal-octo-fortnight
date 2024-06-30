##Robert Fernandez
##Complete
##This program will write a series of random numbers to a file betweeen 1 and 500.

import random

##This will open the file and write the random numbers to the file.
num_numbers = int(input("How many random numbers do you want to generate?: "))

with open('random_numbers.txt', 'w') as file:
    for _ in range(num_numbers):
        file.write(f"{random.randint(1, 500)}\n")
