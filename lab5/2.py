#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example", "r") as file:
        data = file.read()
        print(re.findall(r"\bab{2,3}\b", data))
