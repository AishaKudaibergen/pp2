#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generating():
    for i in range(65, 91):
        l = open(rf"c:\Users\kafka\Documents\Demo\lab6\Directories and Files\26text_files\{chr(i)}.txt", "a")

generating()