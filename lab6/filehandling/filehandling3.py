# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
pathh = input()
if os.path.exists(pathh):
    dir = os.path.dirname(pathh)
    name = os.path.basename(pathh)
    print(f"Path exists! The filename is {name}, in the directory {dir}")
else:
    print("Path doesn't exist")