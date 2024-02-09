import random
x = random.randint(1, 20)
def game():
    name = input("What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    num = cnt = 0
    while num!=x:
        num = int(input('Take a guess.\n'))
        cnt+=1
        if num < x:
            print("\nYou gues is to low")
        elif num > x:
            print("\nYour guess is too high.")
        else:
            return f'\nGood job, {name}! You guessed my number in {cnt} guesses!'
        
        
        

print(game())