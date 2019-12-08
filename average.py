# !/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This gets random numbers then finds the average using an array


import random


def main():
    # Array
    number_array = []

    # Process
    for repeater in range(10):
        random_number = random.randint(1, 100)
        print("Random number " + str(repeater) + " is " + str(random_number))
        number_array.append(random_number)

    average = sum(number_array)/10

    # Output
    print("The answear is " + str(average))


if __name__ == "__main__":
    main()
