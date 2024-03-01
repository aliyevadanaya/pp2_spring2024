#Write a Python program to split a string at uppercase letters.
import re
s = input()
result = re.findall("[A-Z][^A-Z]*", s)
print(result)