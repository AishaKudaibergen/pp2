#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example", "r") as file:
        data = file.read()
        print(re.findall(r"[a-z]+_[a-z]+", data))