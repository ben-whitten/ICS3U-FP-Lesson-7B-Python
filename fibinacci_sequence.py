#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This is a program which displays the first 100 numbers in the fibonacci
# sequence.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def calculations():

    sequence = []
    number_1 = 1
    number_2 = 1
    counter_2 = 0

    for counter_2 in range(1, 100+1):
        answer = number_1 + number_2
        sequence.append(answer)
        number_1 = number_2
        number_2 = answer
    return sequence


def main():
    # This is what runs the program.
    counter = 0
    fibonacci_sequence = []
    fibonacci_sequence = calculations()
    for counter in range(100):
        print(fibonacci_sequence[counter])


if __name__ == "__main__":
    main()
