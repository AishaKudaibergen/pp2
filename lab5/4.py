#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example", "r") as file:
        data = file.read()
        print(re.findall(r"\b[A-Z][a-z]+\b", data))