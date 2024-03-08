# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s = input()
lower = 0
upper = 0
for i in range (0, len(s)):
    if s[i].islower():
        lower+=1
    elif s[i].isupper():
        upper+=1
print(f"This string has {lower} lower letters and {upper} upper letters")
        
        
        