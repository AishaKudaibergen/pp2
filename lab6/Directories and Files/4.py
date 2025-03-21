#Write a Python program to count the number of lines in a text file.
def count(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return len(lines)

file_path = r"c:\Users\kafka\Documents\Demo\lab6\Directories and Files\a.txt"

num_lines = count(file_path)
print(f"{num_lines} lines")
