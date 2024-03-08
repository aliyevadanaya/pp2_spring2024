# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
reverse = "".join(reversed(s))
if s==reverse:
    print("it's a palindrome")
else:
    print("It is not a palindrome")