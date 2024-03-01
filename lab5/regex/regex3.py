#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
s = input()
result = re.findall(r"[a-z]+_[a-z]+", s)
print(result)