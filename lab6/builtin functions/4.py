#Write a Python program that invoke square root function after specific milliseconds.
import time
import math

def program(ms, number):
    time.sleep(ms/1000)
    square = math.sqrt(number)
    print(f"Square root {number} of after {ms} miliseconds is {square:.4f}")

number = int(input("Enter a number: "))
millisecond = int(input("Enter delay in milliseconds: "))
program(millisecond, number)