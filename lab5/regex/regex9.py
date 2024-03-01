#Write a Python program to insert spaces between words starting with capital letters.
import re
s = input()
result = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(result)