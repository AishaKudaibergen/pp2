#Write a Python program to insert spaces between words starting with capital letters.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example2", "r") as file:
    data = file.read()
    x = re.sub(r"([a-z])([A-Z])", r"\1 \2", data)
    print(x)