#Write a Python program to count the number of lines in a text file.
name = input()
f = open(name, "r")
f = list(f)
print(len(f))
