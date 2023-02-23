#/usr/bin/python3
# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the original array except the one at i.

def product(numbers):
    new_numbers = [] # declared an empty array 

    for i in numbers:
        new_product = 1 #Initialized the product to 1

        for j in numbers:
            if j != i:
                new_product = new_product * j
        new_numbers.append(new_product)

    return new_numbers

print(product([10, 5, 4, 20]))
print(product([1, 2, 3, 4]))