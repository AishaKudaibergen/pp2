#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def check(file_path):
    if os.access(file_path, os.F_OK):
        print("Name of a file:", os.path.basename(file_path))
        print("Name of a directory:", os.path.dirname(file_path))
    else:
        print("The path doesn't exist.")

path = r'c:\Users\kafka\Documents\Demo\lab6\Directories and Files\a.txt'
check(path)