#Write a Python program to write a list to a file.
def writing(file_path, list_name):
    with open(file_path, "a") as f:

        for item in list_name:
            f.write(f'{item} ')

list = ['i', 'like', 'my', 'suitcase']

path = r'c:\Users\kafka\Documents\Demo\lab6\Directories and Files\b.txt'

writing(path, list)