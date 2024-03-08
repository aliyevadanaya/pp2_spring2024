# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
pathh = input()
if os.path.exists(pathh):
    os.remove(pathh)
    print("I've just deleted the file")
else:
    print("I haven't found it")