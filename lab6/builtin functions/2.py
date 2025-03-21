# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count


text = input("")
upper, lower = count(text)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
