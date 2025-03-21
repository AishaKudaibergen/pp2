#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

path = r"c:\Users\kafka\Documents\Demo"

all = os.listdir(path)
print("All directories and files:",all)

directories = [item for item in all if os.path.isdir(os.path.join(path, item))]
print("Directories:", directories)

files = [item for item in all if os.path.isfile(os.path.join(path, item))]
print('Files:',files)