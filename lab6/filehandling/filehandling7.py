# Write a Python program to copy the contents of a file to another file
name1 = input()
name2 = input()
f = open(name1, "r")
text = f.read()
f.close()
fs = open (name2, "a")
fs.write("\n" + text)
fs.close()