# Create a generator that generates the squares of numbers up to some number N.
def squares_generator(N):
    for i in range(N):
        yield i*i
        
N = int(input())
for i in squares_generator(N):
    print(i)