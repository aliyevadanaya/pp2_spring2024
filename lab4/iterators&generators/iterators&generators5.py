# Implement a generator that returns all numbers from (n) down to 0.
def reversee(n):
    for i in range(n, -1, -1):
        yield i
        
        
num = int(input())
for j in reversee(num):
    print(j)
    