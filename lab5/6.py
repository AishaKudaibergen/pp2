# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example2", "r") as file:
    data = file.read()
    print(re.sub(r"[ ,.]", ":", data))