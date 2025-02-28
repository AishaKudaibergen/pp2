#Write a Python program to convert a given camel case string to snake case.
import re
with open(r"c:\Users\kafka\Documents\Demo\lab5\example2", "r") as file:
    data = file.read().strip()
    x = re.sub(r"([a-z])([A-Z])", r"\1 \2", data)
    x = re.split(" ", x)
    snake_case = "_".join(word.lower() for word in x)
    print(snake_case)