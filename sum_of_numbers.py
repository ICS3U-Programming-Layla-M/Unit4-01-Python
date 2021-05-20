#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 20, 2021
# This program asks the user to input a number
# and displays the sum of all number from 0 to the
# number inputted

def main():
    counter = 0
    sum = 0

    # ask user for number
    number_as_string = input("Enter a positive number: ")

    try:
        # convert from string to integer
        number_as_int = int(number_as_string)

        if (number_as_int < 0):
            # check if number is negative
            print("{} is not a positive number.". format(number_as_int))

        else:
            while counter <= number_as_int:
                # calculate the sum of numbers from 0 to number_as_int
                print("Tracking {} times through loop.". format(counter))
                sum = sum + counter
                counter = counter + 1
            print("{0} is the sum of all the numbers from\
 0 to {1}.". format(sum, number_as_int))
    except ValueError:
        # error message
        print("{} is not a positive number.". format(number_as_string))


if __name__ == "__main__":
    main()
