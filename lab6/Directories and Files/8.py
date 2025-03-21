#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def deleting(file_path):
    if os.access(file_path, os.X_OK):
        print("The path exists.")
        os.remove(file_path)
        print("The file deleted.")
    else:
        print("The path doesn't exist.")

path = r"c:\Users\kafka\Documents\Demo\lab6\Directories and Files\delete_me.txt"
deleting(path)