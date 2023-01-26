#!/usr/bin/python3
# This file checks for any two items on a list, adds them up and compares the result to a given variable
# If the two numbers exists, the numbers are printed out on the screen
numbers = [2, 5, 8, 3, 10, 15, 7, 12]
target = 15
for x in numbers:
    for y in numbers:
        if x+y == target:
            print(x, y)