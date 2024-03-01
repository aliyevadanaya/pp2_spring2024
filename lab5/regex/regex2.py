#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
s = input()
if re.search("ab{2,3}$", s):
    print(True)
else:
    print(False) 
