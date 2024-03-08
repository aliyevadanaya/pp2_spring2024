#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
def checking(pathh):
    if os.path.exists(pathh):
        print("The way exists")
    else:
        print("The way doesn't exist")

    if os.access(pathh, os.R_OK):
        print("I can read the files")
    else:
        print("I can't read the file")
    if os.access(pathh, os.W_OK):
        print("I can write smth")
    else:
        print("I can't write something")
    if os.access(pathh, os.X_OK):
        print("It is executability ")
    else:
        print("It isn't executability")
        
way = r"C:\Users\aliev\OneDrive\Рабочий стол\python\lab6\documents!"
checking(way)