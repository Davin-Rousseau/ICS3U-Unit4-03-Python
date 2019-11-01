#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program uses a for loop
# To calculate the square of all numbers from zero
# to a given number


def main():
    # This function Calculates the square using a for loop
    loop_counter = 0
    answer = 0

    # input
    number = input("Enter a positive integer: ")
    print("")

    # process and output
    try:
        numberInput = int(number)
        if numberInput > 0:
            for loop_counter in range(numberInput):
                answer = loop_counter ** 2
                print("{}^2 = {}".format(loop_counter, answer))
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
