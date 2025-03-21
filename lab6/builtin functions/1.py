#Write a Python program with builtin function to multiply all the numbers in a list
import math

def multiply_list(numbers):
    return math.prod(numbers)

numbers = [3, 2, 7, 2]
result = multiply_list(numbers)
print(result)
