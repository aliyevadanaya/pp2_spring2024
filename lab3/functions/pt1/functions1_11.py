def is_palindrome(string):
    a = word[::-1]
    # a = ""
    # for i in range(len(a)-1, -1, -1):
    #     a+=i
        
        
    if a==string:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"
    
    
if __name__=="__main__":
    word = "rabota"
    print(is_palindrome(word))
