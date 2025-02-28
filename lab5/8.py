#Write a Python program to split a string at uppercase letters.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example2", "r") as file:
    data = file.read()
    x = re.split(r"(?=[A-Z])", data)
    print(x)
