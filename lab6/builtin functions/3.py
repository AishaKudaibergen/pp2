# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

text = input("").lower().replace(" ", "") #приводим к нижнему регистру и убираем пробелы


if is_palindrome(text):
    print("Palindrome")
else:
    print("Not palindrome")
