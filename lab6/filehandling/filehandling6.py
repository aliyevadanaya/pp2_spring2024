# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
for i in range (26):
    name = chr(65 + i) + ".txt"
    f = open(name, "x")
    f.close()
 