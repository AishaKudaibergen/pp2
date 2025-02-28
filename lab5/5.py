#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example", "r") as file:
        data = file.read()
        print(re.findall(r"\ba.+b\b", data))