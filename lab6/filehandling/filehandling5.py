# Write a Python program to write a list to a file.
s = input()
s = s.split()
nameofthefile = input()
f = open(nameofthefile, "x")
for i in s:
    f.write(i + " ")
f.close()
f = open(nameofthefile, "r")
print(f.read())
