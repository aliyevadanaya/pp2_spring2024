def is_palindrome(string):
    a = word[::-1]
    if a==string:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"
    
word = "rabota"
print(is_palindrome(word))
