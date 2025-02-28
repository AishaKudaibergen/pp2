#Write a python program to convert snake case string to camel case string.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example2", "r") as file:
    data = file.read().strip()
    x = re.split("_", data)
    camel_case = x[0] + "".join(word.capitalize() for word in x[1:])
    print(camel_case)
