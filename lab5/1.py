#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example", "r") as file:
        data = file.read()
        print(re.findall(r"\ba+b*\b", data))