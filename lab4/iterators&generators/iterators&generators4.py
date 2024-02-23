""" Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values."""
def square_range(a, b):
    for i in range(a, b+1):
        yield i*i
        
a = int(input())
b = int(input())
for i in square_range(a, b):
    print(i)