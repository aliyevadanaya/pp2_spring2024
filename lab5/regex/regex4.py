# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
s = input()
result = re.findall(r"[A-Z][a-z]+", s)
print(result)