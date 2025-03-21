#Write a Python program to copy the contents of a file to another file
def copy(source_path, destination_path):
    with open(source_path, "r") as source:
        content = source.read()

    with open(destination_path, "w") as destination:
        destination.write(content)


source_file = r"c:\Users\kafka\Documents\Demo\lab6\Directories and Files\a.txt"
destination_file = r"c:\Users\kafka\Documents\Demo\lab6\Directories and Files\a copy.txt"

copy(source_file, destination_file)
