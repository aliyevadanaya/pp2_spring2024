# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(n):
        if i%2==0:
            yield i
        else:
            continue
        
n = int(input())
even_numbers = list(even_generator(n))
print(", ".join(map(str, even_numbers)))